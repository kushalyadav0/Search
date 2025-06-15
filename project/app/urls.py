from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns: list[URLPattern] = [
    path('',views.home, name='home'),
    path('search/',views.search_view, name='search'),
    
]