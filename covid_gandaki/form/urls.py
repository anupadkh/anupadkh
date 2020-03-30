from django.urls import path
from django.conf.urls import include, url
from covid_gandaki.form import views as fv

urlpatterns=[
    path('', fv.index, name='index'),
    path('submission', fv.submit_general, name='submit'),
]

app_name = "form"
