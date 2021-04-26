from django.db import models
from django.db.models import UniqueConstraint
from django.conf import settings
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from apps.permissions.models import ResponsibleGroup

class Organization(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.CharField(max_length=4000, blank=True)

    parent = models.ForeignKey(
        "Organization",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children",
    )

    logo = models.ImageField(upload_to="organizations", blank=True, null=True)
    logo_url = models.URLField(null=True, blank=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    # Permission groups
    # All members are added to the primary group
    # Members can be added to groups programatically
    primary_group = models.OneToOneField(to=ResponsibleGroup, on_delete=models.CASCADE)
    groups = models.ManyToManyField(ResponsibleGroup, related_name="organizations")

    users = models.ManyToManyField(
        "users.User",
        related_name="organizations",
        blank=True,
        through="Membership",
        through_fields=("organization", "user"),
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["parent", "name"], name="unique_child_organization_name"
            )
        ]

    def __str__(self):
        return f"{self.name}"


class Membership(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="memberships"
    )
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="members"
    )
    role = models.ForeignKey("Role", on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["user", "organization"], name="unique_member_in_organization"
            )
        ]

    def __str__(self) -> str:
        return f"{self.organization.name}:{self.user.username}"


class Role(models.Model):
    name = models.TextField(max_length=50, default="Medlem", null=False)

    def __str__(self) -> str:
        return f"{self.name}"
