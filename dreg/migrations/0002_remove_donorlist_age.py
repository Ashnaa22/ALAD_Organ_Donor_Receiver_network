# Generated by Django 4.1.7 on 2023-05-28 23:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dreg", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="donorlist",
            name="age",
        ),
    ]