# Generated by Django 5.0 on 2023-12-29 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SupplyInvoice",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("amount_owed", models.DecimalField(decimal_places=2, max_digits=100)),
                ("date_supplied", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Paid", "Paid"),
                            ("Cancelled", "Cancelled"),
                            ("Payment Pending", "Payment Pending"),
                            ("Defaulted", "Defaulted"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="suppliers.supplier",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]