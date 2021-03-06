# Generated by Django 2.2.3 on 2020-04-08 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lb', '0008_officeemployee'),
        ('food_meds', '0006_auto_20200404_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=300)),
                ('rate_equivalent', models.FloatField(default=0.0)),
                ('mun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.Municipality')),
            ],
        ),
    ]
