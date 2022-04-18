# Generated by Django 3.2.3 on 2022-04-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_view', '0003_auto_20220416_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='bill_amount',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='payment',
            name='current_unit',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='penalty',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='payment',
            name='previous_unit',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='payment',
            name='saving_unit',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='payment',
            name='total_unit',
            field=models.IntegerField(max_length=30),
        ),
    ]
