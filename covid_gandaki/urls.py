"""covid_gandaki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views import generic
# from material.frontend import urls as frontend_urls
# from django.conf.urls import url, include

# Serializers define the API representation.

from .routers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', generic.RedirectView.as_view(url='/workflow/', permanent=False)),
    # url(r'', include(frontend_urls)),
    path('', include('covid_gandaki.form.urls')),
    path('users/', include('covid_gandaki.users.urls')),
    path('lb/', include('covid_gandaki.lb.urls')),
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^router/', include((router.urls, 'router'), namespace='router')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('snip/', include('covid_gandaki.snippets.urls')),
    path('dash_counter', include('covid_gandaki.dashboard.urls')),
]
