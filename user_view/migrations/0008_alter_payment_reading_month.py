# Generated by Django 3.2.3 on 2022-05-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_view', '0007_alter_payment_reading_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='reading_month',
            field=models.CharField(choices=[('September', 'September'), ('February', 'February'), ('October', 'October'), ('August', 'August'), ('December', 'December'), ('April', 'April'), ('May', 'May'), ('March', 'March'), ('July', 'July'), ('June', 'June'), ('November', 'November'), ('January', 'January')], max_length=10),
        ),
    ]