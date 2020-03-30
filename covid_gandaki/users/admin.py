from django.contrib import admin
from covid_gandaki.users.models import User
# Register your models here.
# admin.site.register(User)

from django.apps import apps


for x in apps.get_models():
    if 'covid' in str(x):
        admin.site.register(x)