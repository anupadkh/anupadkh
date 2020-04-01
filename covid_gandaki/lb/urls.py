from django.urls import path
from django.conf.urls import include, url
from covid_gandaki.lb import views
from covid_gandaki.public import views as pv

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('submission', views.submit, name='submit'),
    path('dtable', views.index_dtable, name='tabulator'),
    path('food_info', pv.index, name='khadya' ),
]

app_name = "lb"
