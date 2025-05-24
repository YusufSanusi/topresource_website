from django.urls import path

from . import views

urlpatterns = [
    path('', views.Portfolio.as_view(), name='portfolio'),
    path('portfolio-management/', views.PortfolioManagement.as_view(), name='portfolio-management'),
    path('delete-project', views.delete_project, name='delete-project'),
    path('<str:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('example/<str:pk>/', views.project_example, name='project-detail-example'),
]
