# Generated by Django 2.2.3 on 2020-03-30 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='current_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='permanent_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
