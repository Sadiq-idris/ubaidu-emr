# Generated by Django 4.2.7 on 2023-11-15 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0003_visit"),
    ]

    operations = [
        migrations.RenameField(
            model_name="visit",
            old_name="type_title",
            new_name="issue",
        ),
    ]
