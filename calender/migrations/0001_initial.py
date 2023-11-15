# Generated by Django 4.1.5 on 2023-11-14 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0005_alter_facility_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Calender",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("established patient", "Established Patient"),
                            ("in office", "In Office"),
                            ("lunch", "Lunch"),
                            ("new patient", "New Patient"),
                            ("office visit", "Office Visit"),
                            ("put of office", "Out Of Office"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            (" ", " "),
                            ("reminder done", "* Reminder Done"),
                            ("chart pulled", "+ Chart Pulled"),
                            ("cancelled", "x Cancelled"),
                            ("arrived", "@ Arrived"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("time", models.TimeField()),
                ("duration", models.DurationField()),
                (
                    "facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.facility",
                    ),
                ),
            ],
        ),
    ]
