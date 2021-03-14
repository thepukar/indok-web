import graphene
from api.graphql.users.types import UserType
from apps.events.models import Category, Event
from django.core.exceptions import PermissionDenied
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from ..users.types import UserType


class UserAttendingType(graphene.ObjectType):
    is_signed_up = graphene.Boolean()
    is_on_waiting_list = graphene.Boolean()


class EventType(DjangoObjectType):
    user_attendance = graphene.Field(UserAttendingType)
    is_full = graphene.Boolean(source="is_full")
    users_on_waiting_list = graphene.List(UserType)
    users_attending = graphene.List(UserType)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "start_time",
            "end_time",
            "location",
            "description",
            "organization",
            "category",
            "image",
            "is_attendable",
            "deadline",
            "publisher",
            "available_slots",
            "price",
            "signup_open_date",
            "short_description"
        ]

    class PermissionDecorators:
        @staticmethod
        def is_in_event_organization(resolver):
            def wrapper(event: Event, info):
                user = info.context.user
                if user.memberships.filter(organization=event.organization).exists() or user.is_superuser:
                    return resolver(event, info)
                else:
                    raise PermissionError(
                        f"Du må være medlem av organisasjonen {event.organization.name} for å gjøre dette kallet")

            return wrapper

    @staticmethod
    def resolve_user_attendance(event, info):
        user = info.context.user
        return {
            "is_signed_up": user in event.users_attending,
            "is_on_waiting_list": user in event.users_on_waiting_list,
        }

    @staticmethod
    @login_required
    @PermissionDecorators.is_in_event_organization
    def resolve_users_on_waiting_list(event, info):
        return event.users_on_waiting_list

    @staticmethod
    @login_required
    @PermissionDecorators.is_in_event_organization
    def resolve_users_attending(event, info):
        return event.users_attending


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]
