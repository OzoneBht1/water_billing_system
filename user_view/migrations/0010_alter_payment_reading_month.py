# Generated by Django 3.2.3 on 2022-05-02 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_view', '0009_alter_payment_reading_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='reading_month',
            field=models.CharField(choices=[('October', 'October'), ('September', 'September'), ('January', 'January'), ('November', 'November'), ('July', 'July'), ('February', 'February'), ('August', 'August'), ('May', 'May'), ('April', 'April'), ('March', 'March'), ('December', 'December'), ('June', 'June')], max_length=10),
        ),
    ]