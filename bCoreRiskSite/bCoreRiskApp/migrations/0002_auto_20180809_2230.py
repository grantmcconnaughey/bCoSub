# Generated by Django 2.0.5 on 2018-08-09 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bCoreRiskApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskfield',
            name='field_name',
            field=models.CharField(default='garbage', max_length=200),
            preserve_default=False,
        ),
    ]
