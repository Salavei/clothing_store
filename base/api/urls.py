from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('denim/', views.getDenim),
    path('denim/<str:pk>/', views.getDenimDetail),
]