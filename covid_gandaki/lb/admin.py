from django.contrib import admin

# Register your models here.
from covid_gandaki.lb.models import *

admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Hospital)