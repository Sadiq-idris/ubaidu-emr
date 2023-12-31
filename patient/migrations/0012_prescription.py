# Generated by Django 4.1.5 on 2023-11-19 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("patient", "0011_alter_soap_encounter_alter_vitals_encounter"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prescription",
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
                ("currently_active", models.BooleanField()),
                ("starting_date", models.DateField(default=django.utils.timezone.now)),
                ("drug", models.CharField(max_length=200)),
                ("quantity", models.CharField(max_length=200)),
                (
                    "medicine_units",
                    models.CharField(
                        choices=[
                            ("mg", "mg"),
                            ("mg/1cc", "mg/1cc"),
                            ("mg/2cc", "mg/2cc"),
                            ("mg/3cc", "mg/3cc"),
                            ("mg/4cc", "mg/4cc"),
                            ("mg/5cc", "mg/5cc"),
                            ("mcg", "mcg"),
                            ("gram", "gram"),
                        ],
                        max_length=200,
                    ),
                ),
                ("take", models.IntegerField()),
                (
                    "_in",
                    models.CharField(
                        choices=[
                            ("suspension", "suspension"),
                            ("tablet", "tablet"),
                            ("capsule", "capsule"),
                            ("solution", "solution"),
                            ("tsp", "tsp"),
                            ("ml", "ml"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "refills",
                    models.CharField(
                        choices=[
                            ("01", "01"),
                            ("02", "02"),
                            ("03", "03"),
                            ("04", "04"),
                            ("05", "05"),
                            ("06", "06"),
                            ("07", "07"),
                            ("08", "08"),
                            ("09", "09"),
                            ("10", "10"),
                            ("11", "11"),
                            ("12", "12"),
                            ("13", "13"),
                            ("14", "14"),
                            ("15", "15"),
                            ("16", "16"),
                            ("17", "17"),
                            ("18", "18"),
                            ("19", "19"),
                            ("20", "20"),
                        ],
                        max_length=200,
                    ),
                ),
                ("notes", models.TextField()),
                ("add_to_medication_list", models.BooleanField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
