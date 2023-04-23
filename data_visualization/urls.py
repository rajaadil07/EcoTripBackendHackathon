from django.urls import path
from . import views

urlpatterns = [
    path('visualize/', views.visualize_carbon_footprint, name='visualize_carbon_footprint'),
]