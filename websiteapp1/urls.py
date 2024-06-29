"""indiapediawebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('countries',views.countries,name='countries'),
    path('science',views.science,name='science'),
    path('home',views.home,name='home'),
    path('geography', views.geography, name='geography'),
    path('entertainment',views.entertainment,name='entertainment'),
    path('culture',views.culture,name='culture'),
    path('parties',views.parties,name='parties'),
    path('festivals', views.festivals, name='festivals'),
    path('places',views.places,name='places'),
    path('art',views.art,name='art'),
    path('songdancemusic',views.songdancemusic,name='songdancemusic'),
    path('sports', views.sports, name='sports'),
    path('person',views.person,name='person'),
    path('technology',views.technology,name='technology'),
    path('biographies',views.biographies,name='biographies'),
    path('onthisday', views.onthisday, name='onthisday'),
    path('companionst', views.companionst, name='companionst'),
    path('imggal', views.imggal, name='imggal'),
    path('spotlight', views.imggal, name='spotlightcountries'),
    path('searchpedia', views.searchpedia, name='searchpedia'),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
