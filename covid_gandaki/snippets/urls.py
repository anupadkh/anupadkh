from django.urls import path
from covid_gandaki.snippets import views, new_view


urlpatterns = [
    path('snippets/', views.snippet_list,name='travellers'),
    path('hospitals/',views.hospital_list, name='hospital'),
    path('covids', views.covid_list, name = 'covids'),

    path('petrol', views.petrol_list, name='petrol'),
    path('sell/',views.sell_list, name='sell_items'),
    path('medical/',views.medical_list, name='medical_items'),
    path('needy/', views.need_list, name='need_people'),
    path('relief/', views.relief_list, name='relief'),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('create_relief', new_view.relief_list, name='create_relief'),
]
app_name = "snippets"
