# Generated by Django 2.0.5 on 2018-08-09 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bCoreRiskApp', '0004_auto_20180809_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='option',
            new_name='choice_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='field_enum',
        ),
        migrations.AddField(
            model_name='choice',
            name='risk_field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bCoreRiskApp.RiskField'),
            preserve_default=False,
        ),
    ]
