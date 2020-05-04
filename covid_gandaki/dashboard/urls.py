from django.urls import path
from django.conf.urls import include, url
from covid_gandaki.dashboard import views

urlpatterns = [
    path('', views.index, name='landing'),
]

app_name = "dashboard"
