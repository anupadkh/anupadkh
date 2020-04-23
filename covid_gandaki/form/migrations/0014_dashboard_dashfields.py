# Generated by Django 2.2.3 on 2020-04-23 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0013_auto_20200414_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('url', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DashFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('width', models.ImageField(default=100, upload_to='')),
                ('title', models.CharField(max_length=300)),
                ('read_only', models.BooleanField(default=False)),
                ('mask', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('col_type', models.CharField(max_length=60)),
                ('autocomplete', models.BooleanField(blank=True, default=False, null=True)),
                ('url', models.CharField(blank=True, max_length=300, null=True)),
                ('dash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Dashboard')),
            ],
        ),
    ]