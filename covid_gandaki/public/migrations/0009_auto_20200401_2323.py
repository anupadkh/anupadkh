# Generated by Django 2.2.3 on 2020-04-01 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0008_auto_20200401_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]