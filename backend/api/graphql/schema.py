import graphene

from .events.schema import EventMutations, EventQueries
from .listing.schema import ListingMutations, ListingQueries
from .organizations.schema import OrganizationMutations, OrganizationQueries
from .surveys.schema import SurveyQueries, SurveyMutations

class Queries(
    EventQueries,
    ListingQueries,
    OrganizationQueries,
    SurveyQueries,
):
    pass


class Mutations(
    EventMutations,
    ListingMutations,
    OrganizationMutations,
    SurveyMutations,
):
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)
