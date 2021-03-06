# Generated by Django 2.2.3 on 2020-04-02 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lb', '0003_auto_20200330_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=300, null=True)),
                ('ward', models.IntegerField(default=1)),
                ('house_no', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'address2',
            },
        ),
        migrations.CreateModel(
            name='Person2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300, verbose_name='Full Name')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=500, null=True)),
                ('current_address', models.CharField(blank=True, max_length=500, null=True)),
                ('mobile', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('location', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'especial_people_',
            },
        ),
        migrations.AlterField(
            model_name='municipality',
            name='administrator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin', to='lb.Person2'),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='chairman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chair', to='lb.Person2'),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='deputy_chairman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='depchair', to='lb.Person2'),
        ),
        migrations.DeleteModel(
            name='QTPerson',
        ),
        migrations.AddField(
            model_name='address',
            name='mun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lb.Municipality'),
        ),
    ]
