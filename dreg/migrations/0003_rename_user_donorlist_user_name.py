# Generated by Django 4.1.7 on 2023-06-04 20:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dreg", "0002_donorlist_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="donorlist",
            old_name="user",
            new_name="user_name",
        ),
    ]