# Generated by Django 2.2.3 on 2020-04-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0014_dashboard_dashfields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashfields',
            name='width',
            field=models.IntegerField(default=100),
        ),
    ]