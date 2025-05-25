from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
