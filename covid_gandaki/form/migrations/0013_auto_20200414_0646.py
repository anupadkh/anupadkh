# Generated by Django 2.2.3 on 2020-04-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0012_covidcounters_no_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidcounters',
            name='no_person',
            field=models.BooleanField(blank=True, default=0, null=True, verbose_name='COVID-19 को CASE नभएको'),
        ),
    ]
