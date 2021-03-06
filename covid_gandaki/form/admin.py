from django.contrib import admin

# Register your models here.
from covid_gandaki.form.models import Stat, StatValues, StatCounters, Dashboard, DashFields

# admin.site.unregister(Stat)
# admin.site.unregister(StatValues)

class StatInline(admin.TabularInline):
    model=StatValues

class StatCounterInline(admin.TabularInline):
    model = StatCounters

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle')
    list_display_links = ('title', 'subtitle')
    # list_filter = ('is_staff', 'company')
    inlines = [
        StatInline, StatCounterInline
    ]




class DashFieldsInline(admin.TabularInline):
    model = DashFields


@admin.register(Dashboard)
class DashAdmin(admin.ModelAdmin):
    list_display = ('name',)

    inlines = [
        DashFieldsInline
    ]

