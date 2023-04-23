from rest_framework.views import APIView
from rest_framework.response import Response
import googlemaps,openai
from django.conf import settings
from .models import CarbonFootprint
from .serializers import CarbonFootprintSerializer
from rest_framework.generics import ListAPIView

CO2_PER_KM = {
    "car_gasoline": 0.120,  # kg CO2/km
    "car_diesel": 0.130,  # kg CO2/km
    "car_electric": 0.050,  # kg CO2/km
    "bus": 0.080,  # kg CO2/km per passenger
    "train": 0.030,  # kg CO2/km per passenger
    "airplane": 0.250,  # kg CO2/km per passenger
    "biking": 0.010,  # kg CO2/km (indirect emissions)
    "walking": 0.005,  # kg CO2/km (indirect emissions)
}

def chat_gpt_request(origin, destination):
    openai.api_key = settings.OPENAI_API_KEY
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Help me find the most efficient and detailed way to get from {origin} to {destination} in the most efficient way possible, while having the least amount of carbon emissions released. Calculate the estimated amount of carbon emissions released for each form of transportation."
            }
        ]
    )

    chat_response = completion.choices[0].message.content
    return chat_response

class CalculateCarbonFootprint(APIView):
    def post(self, request, *args, **kwargs):
        origin = request.data.get('origin')
        destination = request.data.get('destination')

        print("Received data:", request.data)  # Debugging: print received data

        if not origin or not destination:
            return Response({'error': 'Please provide origin and destination.'}, status=400)
        
        chat_gpt_response = chat_gpt_request(origin, destination)
        print(f'ChatGPT: {chat_gpt_response}')

        # Calculate distance using Google Maps API
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        directions_result = gmaps.directions(origin, destination, mode="driving")

        total_distance = 0
        for leg in directions_result[0]['legs']:
            total_distance += leg['distance']['value']

        total_distance /= 1000  # Convert distance to kilometers

        # Calculate carbon footprint for each mode of transportation
        carbon_footprint = {}
        for mode, emissions in CO2_PER_KM.items():
            carbon_footprint[mode] = total_distance * emissions

        result = {
            'origin': origin,
            'destination': destination,
            'distance': total_distance,
            'carbon_footprint': carbon_footprint
        }

        # Save the data to the database
        carbon_footprint_entry = CarbonFootprint(
            origin=origin,
            destination=destination,
            distance=total_distance,
            car_gasoline=carbon_footprint['car_gasoline'],
            car_diesel=carbon_footprint['car_diesel'],
            car_electric=carbon_footprint['car_electric'],
            bus=carbon_footprint['bus'],
            train=carbon_footprint['train'],
            airplane=carbon_footprint['airplane'],
            biking=carbon_footprint['biking'],
            walking=carbon_footprint['walking'],
            chat_gpt_response=chat_gpt_response,
        )
        carbon_footprint_entry.save()

        print("Saved data:", carbon_footprint_entry)  # Debugging: print saved data

        return Response({'result': result})
    
class GetAllCarbonFootprints(ListAPIView):
    queryset = CarbonFootprint.objects.all()
    serializer_class = CarbonFootprintSerializer