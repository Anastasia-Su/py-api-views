# Generated by Django 4.2.8 on 2023-12-13 21:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0005_actor_full_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="actor",
            name="full_name",
        ),
    ]