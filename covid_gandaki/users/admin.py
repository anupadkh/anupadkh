from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from covid_gandaki.users.models import User, Employee
# Register your models here.


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

admin.site.register(User,UserAdmin )

from django.apps import apps


for x in apps.get_models():
    if 'User' in str(x):
        continue
    if 'covid' in str(x):
        admin.site.register(x)
