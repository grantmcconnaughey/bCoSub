# Generated by Django 2.0.5 on 2018-08-17 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bCoreRiskApp', '0012_auto_20180817_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskfield',
            name='field_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]