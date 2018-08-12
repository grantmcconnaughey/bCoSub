# Generated by Django 2.0.5 on 2018-08-09 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_class', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RiskField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=200, null=True)),
                ('field_text', models.TextField(null=True)),
                ('field_num', models.FloatField(null=True)),
                ('field_date', models.DateTimeField(null=True)),
                ('field_enum_text', models.CharField(max_length=200, null=True)),
                ('risk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bCoreRiskApp.Risk')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='field_enum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bCoreRiskApp.RiskField'),
        ),
    ]