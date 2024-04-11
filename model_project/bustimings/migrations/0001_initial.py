# Generated by Django 4.1.5 on 2023-09-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BusTiming",
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
                ("bus_name", models.CharField(max_length=100)),
                ("departure_time", models.TimeField()),
                ("arrival_time", models.TimeField()),
                ("origin", models.CharField(max_length=100)),
                ("destination", models.CharField(max_length=100)),
            ],
        ),
    ]