# Generated by Django 3.2.3 on 2022-04-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_view", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewTap",
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
                ("province", models.CharField(max_length=100)),
                ("district", models.CharField(max_length=100)),
                ("municipality", models.CharField(max_length=100)),
                ("first_name", models.CharField(max_length=100)),
                ("middle_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("house_no", models.CharField(max_length=100)),
                ("contact_no", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("citizenship", models.ImageField(upload_to="")),
            ],
        ),
    ]
