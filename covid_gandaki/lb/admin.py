from django.contrib import admin

# Register your models here.
from covid_gandaki.lb.models import *
from covid_gandaki.lb.sub_models.rahat import ReliefFund, ReliefItem

admin.site.register(ReliefFund)
admin.site.register(ReliefItem)
# admin.site.register(Municipality)
# admin.site.register(Hospital)