# Generated by Django 3.2.3 on 2022-04-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_view', '0005_auto_20220429_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='phone_num',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='timestamp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='reading_month',
            field=models.CharField(choices=[('August', 'August'), ('July', 'July'), ('June', 'June'), ('January', 'January'), ('September', 'September'), ('February', 'February'), ('April', 'April'), ('March', 'March'), ('December', 'December'), ('October', 'October'), ('May', 'May'), ('November', 'November')], max_length=10),
        ),
    ]