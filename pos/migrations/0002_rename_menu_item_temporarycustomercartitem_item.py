# Generated by Django 4.1.7 on 2023-11-09 14:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="temporarycustomercartitem",
            old_name="menu_item",
            new_name="item",
        ),
    ]
