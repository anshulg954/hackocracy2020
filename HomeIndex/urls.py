from django.contrib import admin
from django.urls import path, include

from . import views 

urlpatterns = [
    path('', views.homePage, name="Home"),
    path('stats/', views.stats)
]

