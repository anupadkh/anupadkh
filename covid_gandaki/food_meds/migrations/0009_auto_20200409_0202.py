# Generated by Django 2.2.3 on 2020-04-09 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_meds', '0008_auto_20200408_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodname',
            name='unit',
            field=models.CharField(max_length=50),
        ),
    ]
