# Generated by Django 2.2.3 on 2020-04-13 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lb', '0011_auto_20200411_1105'),
        ('form', '0009_auto_20200413_0807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stat',
            options={'verbose_name': 'ड्यासबोर्ड सेटिङ्ग र काउन्टर', 'verbose_name_plural': 'ड्यासबोर्डका काउन्टरहरु'},
        ),
        migrations.CreateModel(
            name='CovidCounters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('samples', models.IntegerField(blank=True, default=0, null=True)),
                ('infected', models.IntegerField(blank=True, default=0, null=True)),
                ('death', models.IntegerField(blank=True, default=0, null=True)),
                ('cured', models.IntegerField(blank=True, default=0, null=True)),
                ('result_waiting', models.IntegerField(blank=True, default=0, null=True)),
                ('mun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.Municipality')),
            ],
        ),
    ]