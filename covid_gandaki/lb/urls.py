from django.urls import path
from django.conf.urls import include, url
from covid_gandaki.lb import views
from covid_gandaki.public import views as pv

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('submission', views.submit, name='submit'),
    path('dtable', views.index_dtable, name='dtable'),
    path('food_info', pv.index, name='khadya' ),
    path('<int:id>/dtable', views.list_dtable, name='table_view'),
    path('add_person2/', views.Person2CreateView.as_view(), name="add_person2"),
    path('<int:id>/reliefperson', views.reliefs, name='relief')

]

app_name = "lb"
