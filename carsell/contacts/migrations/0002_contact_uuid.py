# Generated by Django 4.1.3 on 2022-12-06 11:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]