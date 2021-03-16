# Generated by Django 3.1.2 on 2021-03-16 16:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0026_auto_20210316_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='id',
        ),
        migrations.AlterField(
            model_name='answer',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
