# Generated by Django 3.1.8 on 2021-08-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0030_auto_20210426_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='org_page_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
