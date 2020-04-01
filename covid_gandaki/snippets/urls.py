from django.urls import path
from covid_gandaki.snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
app_name = "snippets"
