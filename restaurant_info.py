import pip._vendor.requests
import json

# Put your API key here
api_key = 'YOUR_API_KEY'

# Function to get restaurant information from Google Maps Places API
def get_restaurant_info(place_id):
    url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,types,permanently_closed&key={api_key}'
    response = pip._vendor.requests.get(url)
    restaurant_info = json.loads(response.text)
    return restaurant_info

# Function to get the types of food a restaurant serves
def get_food_types(place_id):
    restaurant_info = get_restaurant_info(place_id)
    if 'types' in restaurant_info['result']:
        food_types = [type for type in restaurant_info['result']['types']]
        return food_types
    else:
        return None

# Example usage
place_id = 'ChIJEy05P-fHwoAR1eHcd5k0UWs'
food_types = get_food_types(place_id)
print(food_types)

if food_types == None:
    print("No information about food types or restaurant is closed permanently")
else:
    print(food_types)

#Enable the Google Places API on Google Cloud Console.
