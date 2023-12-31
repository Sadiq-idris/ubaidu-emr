# Generated by Django 4.2.7 on 2023-11-22 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0016_insurancecompany"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="insurance_company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="patient.insurancecompany",
            ),
        ),
    ]
