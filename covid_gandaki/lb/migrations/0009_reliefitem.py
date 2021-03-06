# Generated by Django 2.2.3 on 2020-04-08 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_meds', '0007_foodname'),
        ('lb', '0008_officeemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReliefItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField(default=0)),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_meds.FoodName')),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.ReliefFund')),
            ],
        ),
    ]
