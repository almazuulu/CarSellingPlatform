# Generated by Django 4.1.3 on 2022-12-03 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Teams", new_name="Team",),
        migrations.AlterModelOptions(
            name="team",
            options={"verbose_name": "Team", "verbose_name_plural": "Teams"},
        ),
    ]
