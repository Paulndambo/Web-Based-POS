# Generated by Django 5.0 on 2023-12-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0003_remove_supplyinvoice_amount_owed_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="supplyinvoice",
            name="date_due",
            field=models.DateField(null=True),
        ),
    ]