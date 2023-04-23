from django.http import JsonResponse
from carbon_footprint.views import CO2_PER_KM, CalculateCarbonFootprint
from rest_framework.request import Request

class CustomRequest(Request):
    def __init__(self, request, data):
        super().__init__(request)
        self._data = data

    @property
    def data(self):
        return self._data

# Create your views here.
def visualize_carbon_footprint(request):
    # Use the CalculateCarbonFootprint class from the carbon_footprint app
    calculate_carbon_footprint = CalculateCarbonFootprint()
    
    # Create a custom request to call the post method of the CalculateCarbonFootprint class
    custom_request = CustomRequest(request, {
        'origin': 'New York, NY',
        'destination': 'Los Angeles, CA',
    })

    # Retrieve carbon footprint data
    response = calculate_carbon_footprint.post(custom_request)
    
    if response.status_code == 200:
        # Extract data for each form of transportation
        transportation_modes = list(CO2_PER_KM.keys())
        carbon_footprint = response.data['result']['carbon_footprint']
        
        # Calculate total emissions for each mode
        total_emissions = {mode: carbon_footprint[mode] for mode in transportation_modes}
    else:
        total_emissions = {'error': 'Failed to calculate carbon footprint'}

    return JsonResponse(total_emissions)
