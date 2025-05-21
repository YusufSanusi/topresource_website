from django.urls import path

from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('portfolio-management/', views.portfolio_management, name='portfolio_management'),
    path('delete-project', views.delete_project, name='delete_project'),
]
