from django.urls import path
from django.conf.urls import include, url
from covid_gandaki.dashboard import views

urlpatterns = [
    path('index/', views.index, name='landing'),
    path('<int:id>/', views.index, name="navigate"),
]

app_name = "dashboard"
