# Generated by Django 3.1.2 on 2021-03-14 15:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("organizations", "0016_auto_20210308_2014"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="users",
            field=models.ManyToManyField(
                blank=True,
                related_name="organizations",
                through="organizations.Membership",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
