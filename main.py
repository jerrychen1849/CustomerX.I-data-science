# Yelp API 
# Information found at this link: https://docs.developer.yelp.com/docs/fusion-intro
import requests
import json

# Set API endpoint and API key
endpoint = "https://api.yelp.com/v3/businesses/search"
headers = {
   #"Authorization": "Bearer YOUR_API_KEY"
    "Authorization": "Bearer Kg93JEhI3PlbRx2hy3_FmmHBxE13vy9F0YKGHO7q8jMtUm370WobSxQeNTjxow5-Cky79eCGntdsddYiTrGptrPEsQAKMf40i2RKB0-rvRLZzLnwq83tauVBVYDRY3Yx"
}

# Here we set the parameters. 
# Enter term (name of restaurant) e.g. "Applebee's" or "Jamba Juice"
# Enter location e.g. "San Francisco" or "New York City" or even zip code
params = {
    "term": "",
    "location": ""
}

# Make API request
response = requests.get(endpoint, headers=headers, params=params)

# Parse JSON response
data = json.loads(response.text)

# Create an empty set to store unique categories
unique_categories = set()

# Extract and print all unique categories
for business in data["businesses"]:
    for category in business["categories"]:
        unique_categories.add(category["title"])

for index in unique_categories:
    print(index)
