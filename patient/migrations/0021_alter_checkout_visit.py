# Generated by Django 4.2.7 on 2023-11-22 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0020_alter_checkout_visit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkout",
            name="visit",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="checkout",
                to="patient.visit",
            ),
        ),
    ]
