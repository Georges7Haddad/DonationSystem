# Generated by Django 3.0.3 on 2020-11-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodDonation', '0007_auto_20201116_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='phone_number',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='phone_number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
