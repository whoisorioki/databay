import requests
import json

# Make a get request to get the latest position of the ISS from the OpenNotify API.
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)
print(response.json())

# Make a get request to get the number of people in ISS from the OpenNotify API.
response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)
print(response.headers['Content-Type'])
print(response.json()['number'])

# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

# Convert best_food_chains_string back to a list.
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))

# Loading a string to JSON format
fast_food_franchise_2 = json.loads(fast_food_franchise_string)
print(type(fast_food_franchise_2))