# Generated by Django 2.2.3 on 2020-04-07 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0015_auto_20200404_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
