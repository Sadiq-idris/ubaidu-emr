# Generated by Django 4.2.7 on 2023-11-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calender", "0006_rename_user_calender_provider_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calender",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="calender",
            name="duration",
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="calender",
            name="time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
