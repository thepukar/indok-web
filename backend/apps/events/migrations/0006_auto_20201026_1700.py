# Generated by Django 3.1.1 on 2020-10-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20201026_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
