# Generated by Django 2.2.3 on 2020-03-30 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('public', '0002_auto_20200330_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=300)),
                ('nep_name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('total_beds', models.IntegerField(default=1)),
                ('ward', models.IntegerField(default=1)),
                ('is_quarantine', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mun_name', models.CharField(max_length=300)),
                ('nep_name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QTPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_postive', models.BooleanField(default=False)),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='public.Person')),
                ('quarantined_zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lb.Hospital')),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='mun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lb.Municipality'),
        ),
        migrations.CreateModel(
            name='CovidCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_cases', models.IntegerField(default=0)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lb.Hospital')),
                ('mun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.Municipality')),
            ],
        ),
    ]
