# Generated by Django 2.2.3 on 2020-03-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_auto_20200330_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
