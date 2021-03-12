from datetime import datetime

import graphene
from apps.events import models
from apps.users.models import User
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from .mail import send_event_emails
from .types import CategoryType, EventType


class EventInput(graphene.InputObjectType):
    title = graphene.String(required=False)
    start_time = graphene.DateTime(required=False)
    end_time = graphene.DateTime(required=False)
    location = graphene.String(required=False)
    description = graphene.String(required=False)
    organization_id = graphene.ID(required=False)
    category_id = graphene.ID(required=False)
    image = graphene.String(required=False)
    is_attendable = graphene.Boolean(required=False)
    deadline = graphene.DateTime(required=False)
    available_slots = graphene.Int(required=False)
    price = graphene.Float(required=False)


class CreateEvent(graphene.Mutation):
    ok = graphene.Boolean()
    event = graphene.Field(EventType)

    class Arguments:
        event_data = EventInput(required=True)

    @login_required
    def mutate(self, info, event_data):
        event = models.Event()
        for k, v in event_data.items():
            setattr(event, k, v)
        event.publisher = info.context.user
        event.save()
        ok = True
        return CreateEvent(event=event, ok=ok)


class UpdateEvent(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        event_data = EventInput(required=False)

    ok = graphene.Boolean()
    event = graphene.Field(EventType)

    def mutate(self, info, event_data):
        event = models.Event.objects.get(pk=id)
        for k, v in event_data.items():
            setattr(event, k, v)
        event.save()
        ok = True
        return UpdateEvent(event=event, ok=ok)


class DeleteEvent(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()
    event = graphene.Field(EventType)

    def mutate(self, info, id):
        event = get_object_or_404(models.Event, pk=id)
        event.delete()
        ok = True
        return DeleteEvent(event=event, ok=ok)


class EventSignUpOrOffInput(graphene.InputObjectType):
    user_id = graphene.ID(required=True)


class EventSignUp(graphene.Mutation):
    class Arguments:
        event_id = graphene.ID(required=True)
        user_id = graphene.ID(required=True)

    is_full = graphene.Boolean()
    event = graphene.Field(EventType)

    def mutate(self, info, event_id, user_id):
        event = models.Event.objects.get(pk=event_id)
        user = User.objects.get(pk=user_id)

        event.signed_up_users.add(user)
        event.save()

        return EventSignUp(event=event, is_full=event.is_full)


class EventSignOff(graphene.Mutation):
    class Arguments:
        event_id = graphene.ID(required=True)
        user_id = graphene.ID(required=True)

    is_full = graphene.Boolean()
    event = graphene.Field(EventType)

    def mutate(self, info, event_id, user_id):
        event = models.Event.objects.get(pk=event_id)
        user = User.objects.get(pk=user_id)

        event.signed_up_users.remove(user)
        event.save()

        return EventSignOff(event=event, is_full=event.is_full)


class CategoryInput(graphene.InputObjectType):
    name = graphene.String(required=False)


class CreateCategory(graphene.Mutation):
    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    class Arguments:
        category_data = CategoryInput(required=True)

    def mutate(self, info, category_data):
        category = models.Category()
        for k, v in category_data.items():
            setattr(category, k, v)
        category.save()
        ok = True
        return CreateCategory(category=category, ok=ok)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        category_data = CategoryInput(required=False)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    def mutate(self, info, category_data):
        category = models.Category.objects.get(pk=id)
        for k, v in category_data.items():
            setattr(category, k, v)
        category.save()
        ok = True
        return UpdateCategory(category=category, ok=ok)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    def mutate(self, info, id):
        category = get_object_or_404(models.Category, pk=id)
        category.delete()
        ok = True
        return DeleteCategory(category=category, ok=ok)


class SendEventEmails(graphene.Mutation):
    class Arguments:
        receiverEmails = graphene.List(graphene.String)
        content = graphene.String()
        subject = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, receiverEmails, content, subject):

        send_event_emails(info, receiverEmails, content, subject)

        ok = True
        return SendEventEmails(ok=ok)