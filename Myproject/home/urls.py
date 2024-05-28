# home/urls.py

from django.urls import path
from home import views

print("Loading home.urls...")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('adminpage/', views.adminpage, name='adminpage')
]
