# Generated by Django 4.2.7 on 2023-11-15 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("patient", "0008_alter_visit_patient"),
    ]

    operations = [
        migrations.AddField(
            model_name="visit",
            name="provider",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="visit",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="patient.patient"
            ),
        ),
    ]
