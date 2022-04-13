# Generated by Django 3.2.3 on 2022-04-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('province', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=100)),
                ('customer_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('previous_unit', models.CharField(max_length=30)),
                ('current_unit', models.CharField(max_length=30)),
                ('saving_unit', models.CharField(max_length=30)),
                ('meter_status', models.BooleanField(default=True)),
                ('bill_amount', models.CharField(max_length=30)),
                ('penalty', models.CharField(max_length=30)),
                ('total_unit', models.CharField(max_length=30)),
            ],
        ),
    ]
