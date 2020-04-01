from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from covid_gandaki.users.models import User
# Register your models here.
admin.site.register(User,UserAdmin )

from django.apps import apps


for x in apps.get_models():
    if 'User' in str(x):
        continue
    if 'covid' in str(x):
        admin.site.register(x)
