# Generated by Django 3.2.3 on 2022-05-02 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_view', '0008_alter_payment_reading_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='reading_month',
            field=models.CharField(choices=[('September', 'September'), ('August', 'August'), ('May', 'May'), ('December', 'December'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('June', 'June'), ('January', 'January'), ('July', 'July'), ('November', 'November'), ('October', 'October')], max_length=10),
        ),
    ]