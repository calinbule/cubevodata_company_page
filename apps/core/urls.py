from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('microservers/', views.microservers, name='microservers'),
    path('cookies/', views.cookies, name='cookies'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]