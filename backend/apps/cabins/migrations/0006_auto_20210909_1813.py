# Generated by Django 3.2.5 on 2021-09-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabins', '0005_booking_cabins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cabin',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
