# Generated by Django 2.2.3 on 2020-03-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb', '0002_auto_20200330_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='district_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
