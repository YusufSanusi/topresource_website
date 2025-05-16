from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    # path('testimonials/', views.testimonials, name='testimonials'),
    path('services/', views.services, name='services'),
    # path('lead-magnet/', views.lead_magnet, name='lead_magnet'),
    path('contact/', views.contact, name='contact'),
    # path('about', views.about, name='about'),
]
