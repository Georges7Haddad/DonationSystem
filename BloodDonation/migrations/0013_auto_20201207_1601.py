# Generated by Django 3.0.3 on 2020-12-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodDonation', '0012_auto_20201207_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='hospital',
            field=models.CharField(max_length=100),
        ),
    ]
