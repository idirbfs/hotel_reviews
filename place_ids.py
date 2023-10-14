import requests
import json
import time

# GET HOTELS IDS 


# Replace with your API key
API_KEY = "AIzaSyApeXWJE5MSQ8mapOkNOgitzfOxhgiOm_o"

# Paris coordinates
paris_location = "48.866669,2.33333"

# Define parameters for the nearby search
url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=hotel&location={paris_location}&type=hotel&key={API_KEY}&rankby=distance'

hotel_ids = []

# Make the initial API request
response = requests.get(url)
data = response.json()

# Extract hotel IDs from the first page
hotel_ids.extend([place['place_id'] for place in data.get('results', [])])

# Handle additional pages
while 'next_page_token' in data:
    # Wait for a few seconds before making the next request
    time.sleep(2)

    # Make the next API request using the next_page_token
    next_page_url = f'{url}&pagetoken={data["next_page_token"]}'
    response = requests.get(next_page_url)
    data = response.json()

    # Extract hotel IDs from the current page
    hotel_ids.extend([place['place_id'] for place in data.get('results', [])])

    # Break the loop if we have enough hotel IDs
    if len(hotel_ids) >= 1000:
        break

# Write the hotel IDs to a JSON file
with open('paris_hotels.json', 'w', encoding='utf-8') as json_file:
    json.dump(hotel_ids, json_file, ensure_ascii=False, indent=2)

print(f"Saved {len(hotel_ids)} Paris hotel IDs to paris_hotels.json")
