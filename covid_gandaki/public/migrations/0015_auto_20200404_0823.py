# Generated by Django 2.2.3 on 2020-04-04 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lb', '0008_officeemployee'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('public', '0014_qtperson_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='needy',
            old_name='name',
            new_name='person',
        ),
        migrations.AddField(
            model_name='needy',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='needy',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='needy',
            name='municipality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lb.Municipality'),
        ),
    ]
