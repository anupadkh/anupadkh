from django.urls import path
from covid_gandaki.snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('hospitals/',views.hospital_list, name='hospital'),
    path('covids', views.covid_list, name = 'covids'),
    
    path('petrol', views.petrol_list, name='petrol'),
    path('sell/',views.sell_list, name='sell_items'),
    path('medical/',views.medical_list, name='medical_items'),
    path('needy/', views.need_list, name='need_people'),

    path('snippets/<int:pk>/', views.snippet_detail),
]
app_name = "snippets"
