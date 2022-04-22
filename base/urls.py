from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delivery/', views.delivery, name='delivery'),
    path('contact/', views.contact, name='contact'),

    path('api/v1/', include('base.api.urls')),
]
