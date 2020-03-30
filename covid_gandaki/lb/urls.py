from django.urls import path
from django.conf.urls import include, url
from covid_gandaki.lb import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('submission', views.submit, name='submit'),
]

app_name = "lb"
