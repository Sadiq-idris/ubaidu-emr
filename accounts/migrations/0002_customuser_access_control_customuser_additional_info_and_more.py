# Generated by Django 4.1.5 on 2023-11-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="access_control",
            field=models.CharField(
                blank=True,
                choices=[
                    ("accounting", "Accounting"),
                    ("administrators", "Administrators"),
                    ("clinicians", "Clinicians"),
                    ("front office", "Front Office"),
                    ("physicians", "Physicians"),
                ],
                max_length=200,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="additional_info",
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="authorized",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="federal_tax_id",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="job_description",
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
