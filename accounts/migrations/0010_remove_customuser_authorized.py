# Generated by Django 4.2.7 on 2023-11-19 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_alter_customuser_access_control"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="authorized",
        ),
    ]
