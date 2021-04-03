import graphene
from graphql_jwt.decorators import login_required
from utils.decorators import permission_required
from guardian.shortcuts import assign_perm, remove_perm

from apps.listing.models import Listing
from apps.surveys.models import Survey
from ..types import SurveyType


class SurveyInput(graphene.InputObjectType):
    name = graphene.String(required=False)
    organization_id = graphene.ID(required=False)
    description = graphene.String(required=False)


class BaseSurveyInput(graphene.InputObjectType):
    name = graphene.String()
    organization_id = graphene.ID()
    description = graphene.String()


class CreateSurveyInput(BaseSurveyInput):
    name = graphene.String(required=True)


class CreateSurvey(graphene.Mutation):
    survey = graphene.Field(SurveyType)
    ok = graphene.Boolean()

    class Arguments:
        listing_id = graphene.ID()
        survey_data = CreateSurveyInput(required=True)

    @login_required
    @permission_required("surveys.add_survey")
    def mutate(self, info, survey_data, listing_id=None):
        survey = Survey()
        for key, value in survey_data.items():
            setattr(survey, key, value)
        survey.save()
        if listing_id:
            listing = Listing.objects.get(pk=listing_id)
            listing.survey = survey
            listing.save()
        
        # Assign permission to the responsible group
        for perm in ["surveys.update_survey", "surveys.delete_survey"]:
            assign_perm(perm, survey.responsible_group, survey)
        return CreateSurvey(survey=survey, ok=True)


class UpdateSurvey(graphene.Mutation):
    survey = graphene.Field(SurveyType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()
        survey_data = BaseSurveyInput(required=True)

    @login_required
    @permission_required("surveys.update_survey", lookup_variables=(Survey, "pk", "id"))
    def mutate(self, info, id, survey_data):
        survey = Survey.objects.get(pk=id)
        old_group = survey.group
        for key, value in survey_data.items():
            setattr(survey, key, value)
        survey.save()
        new_group = survey.group
        if old_group != new_group:
            for perm in ["surveys.update_survey", "surveys.delete_survey"]:
                remove_perm(perm, old_group, survey)
                assign_perm(perm, new_group, survey)
        return UpdateSurvey(survey=survey, ok=True)


class DeleteSurvey(graphene.Mutation):
    deleted_id = graphene.ID()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    @login_required
    @permission_required("surveys.delete_survey", lookup_variables=(Survey, "pk", "id"))
    def mutate(cls, self, info, id):
        survey = Survey.objects.get(pk=id)
        deleted_id = survey.id
        survey.delete()
        return DeleteSurvey(deleted_id=deleted_id, ok=True)
