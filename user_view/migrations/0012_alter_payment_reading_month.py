# Generated by Django 3.2.3 on 2022-05-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_view', '0011_alter_payment_reading_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='reading_month',
            field=models.CharField(choices=[('January', 'January'), ('April', 'April'), ('June', 'June'), ('August', 'August'), ('October', 'October'), ('February', 'February'), ('November', 'November'), ('July', 'July'), ('September', 'September'), ('December', 'December'), ('May', 'May'), ('March', 'March')], max_length=10),
        ),
    ]