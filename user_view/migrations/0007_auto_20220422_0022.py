# Generated by Django 3.2.3 on 2022-04-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_view', '0006_auto_20220418_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='total_unit',
            new_name='total_amount',
        ),
        migrations.AddField(
            model_name='payment',
            name='discount_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='penalty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
