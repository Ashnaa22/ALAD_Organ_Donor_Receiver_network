# Generated by Django 4.1.7 on 2023-06-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dreg", "0005_alter_donorlist_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donorlist",
            name="organ",
            field=models.CharField(
                blank=True,
                choices=[
                    ("one_kidney", "One_Kidney"),
                    ("a_Single_lob_from_lung", "A_Single_lob_from_lung"),
                    ("a_portion_of_liver", "A_portion_of_liver"),
                    ("a_portion_of_pancreas", "A_portion_of_Pancreas"),
                    ("a_portion_of_intestine", "A_portion_of_intestine"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
