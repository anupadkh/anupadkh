# Generated by Django 2.2.3 on 2020-03-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200330_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nepali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=100)),
                ('fieldname', models.CharField(max_length=100)),
                ('nepali_name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
