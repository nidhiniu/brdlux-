# Generated by Django 5.1.4 on 2025-01-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0002_alter_car_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')], default='Petrol', max_length=10, null=True),
        ),
    ]
