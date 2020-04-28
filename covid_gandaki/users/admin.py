from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from covid_gandaki.users.models import User, Employee
from django.contrib.auth.models import Group

# Register your models here.


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

admin.site.register(User,UserAdmin )

admin.site.unregister(Group)


from django.apps import apps


for x in apps.get_models():
    if 'User' in str(x):
        continue
    if 'viewflow' in str(x):
        admin.site.unregister(x)
    # try:
    #     if 'django_q' in str(x):
    #         admin.site.unregister(x)
    # except:
    #     pass
    
