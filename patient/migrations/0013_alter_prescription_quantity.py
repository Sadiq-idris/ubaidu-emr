# Generated by Django 4.1.5 on 2023-11-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0012_prescription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prescription",
            name="quantity",
            field=models.IntegerField(max_length=200),
        ),
    ]
