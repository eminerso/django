from django.contrib import admin
from django.urls import path,include
from .views import items_page




urlpatterns = [

    path("gf",items_page)
    
    
]