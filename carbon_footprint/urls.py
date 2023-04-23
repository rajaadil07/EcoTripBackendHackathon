# urls.py
from django.urls import path
from .views import CalculateCarbonFootprint, GetAllCarbonFootprints

urlpatterns = [
    path('calculate/', CalculateCarbonFootprint.as_view(), name='calculate_carbon_footprint'),
    path('all/', GetAllCarbonFootprints.as_view(), name='get_all_carbon_footprints'),
]