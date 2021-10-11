# Generated by Django 3.2.5 on 2021-10-11 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0033_merge_0031_auto_20210909_1813_0032_auto_20210824_1457'),
        ('blogs', '0002_rename_publishdate_blogpost_publish_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog', to='organizations.organization')),
            ],
        ),
    ]
