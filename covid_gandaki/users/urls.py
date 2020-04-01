from django.urls import path
from django.conf.urls import include, url
from covid_gandaki.users import views 

urlpatterns = [
    # path('', fv.index, name='index')
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.login_view, name='login'),
]

app_name = "users"
