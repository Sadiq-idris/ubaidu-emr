# Generated by Django 4.1.5 on 2023-11-21 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_remove_customuser_authorized"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
