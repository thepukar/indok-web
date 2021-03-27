import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from utils.decorators import permission_required


class UserType(DjangoObjectType):
    grade_year = graphene.Int(source="grade_year")
    events = graphene.List("api.graphql.events.types.EventType", source="events")

    class Meta:
        model = get_user_model()

        fields = [
            "id",
            "last_login",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
            "feide_userid",
            "feide_email",
            "id_token",
            "allergies",
            "phone_number",
            "first_login",
            "graduation_year",
            "memberships",
            "events",
            "organizations",
        ]

    
    @staticmethod
    @login_required
    @permission_required("users.view_sensitive_info", obj_arg_pos=0)
    def resolve_allergies(user, info):
        return user.allergies
