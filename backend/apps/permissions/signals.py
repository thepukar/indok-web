from uuid import uuid4
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.db.models import Q
from django.db.models.signals import post_migrate, pre_save
from django.dispatch import receiver
from apps.organizations.models import Organization

from apps.permissions.constants import (
    DEFAULT_INDOK_PERMISSIONS,
    DEFAULT_ORGANIZATION_PERMISSIONS,
    DEFAULT_REGISTERED_USER_PERMISSIONS,
    INDOK,
    ORGANIZATION,
    REGISTERED_USER,
)
from apps.permissions.models import ResponsibleGroup

User = get_user_model()


@receiver(pre_save, sender=ResponsibleGroup)
def create_named_group(sender, instance: ResponsibleGroup, **kwargs):
    try:
        group = instance.group
    except Group.DoesNotExist:
        try:
            prefix: str = instance.hr_organization.name
        except Organization.DoesNotExist:
            prefix: str = instance.organization.name

        group = Group.objects.create(name=f"{prefix}:{instance.name}:{uuid4().hex}")
        instance.group = group


@receiver(post_migrate)
def assign_standard_organization_permissions(**kwargs):
    """
    Assigns default organization permissions to all users in an organization
    """
    group, _ = Group.objects.get_or_create(name=ORGANIZATION)
    query: Q = Q()

    for perm in DEFAULT_ORGANIZATION_PERMISSIONS:
        query |= Q(content_type__app_label=perm[0], codename=perm[1])

    permissions = Permission.objects.filter(query)
    group.permissions.set(permissions)
    group.user_set.set(User.objects.exclude(username=settings.ANONYMOUS_USER_NAME).exclude(organizations=None))


@receiver(post_migrate)
def assign_standard_permissions(**kwargs):
    """
    Assigns default permissions to all authenticated users
    """
    indok_group, _ = Group.objects.get_or_create(name=INDOK)
    registered_user_group, _ = Group.objects.get_or_create(name=REGISTERED_USER)

    indok_query: Q = Q()
    for perm in DEFAULT_INDOK_PERMISSIONS:
        indok_query |= Q(content_type__app_label=perm[0], codename=perm[1])

    registered_query: Q = Q()
    for perm in DEFAULT_REGISTERED_USER_PERMISSIONS:
        registered_query |= Q(content_type_app_label=perm[0], codename=perm[1])

    indok_permissions = Permission.objects.filter(indok_query)
    indok_group.permissions.set(indok_permissions)

    registered_permissions = Permission.objects.filter(registered_query)
    registered_user_group.permissions.set(registered_permissions)

    users = User.objects.exclude(username=settings.ANONYMOUS_USER_NAME)
    registered_user_group.user_set.set(users)
    indok_group.user_set.set(users.exclude(indok=False))
