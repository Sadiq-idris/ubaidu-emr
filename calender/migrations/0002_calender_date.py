# Generated by Django 4.2.7 on 2023-11-14 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calender", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="calender",
            name="date",
            field=models.DateField(default="2001-12-23"),
        ),
    ]
