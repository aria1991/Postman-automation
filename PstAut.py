# Import the necessary libraries
import os
import json
from postman_api import PostmanAPI
import requests

# Initialize the PostmanAPI object with your API key
api_key = "YOUR_API_KEY"
postman = PostmanAPI(api_key)

# Define the list of APIs that you want to add to Postman
api_list = []

# Read the APIs from a JSON file
with open("apis.json", "r") as f:
    api_list = json.load(f)

# Create a Postman collection to store the APIs
collection_name = "My Collection"
try:
    collection = postman.collections.create(name=collection_name)
    collection_id = collection["id"]
except Exception as e:
    print(f"Error creating collection: {e}")

# Add the APIs to the collection
for api in api_list:
    try:
        postman.requests.create(collection_id=collection_id, data=api)
    except Exception as e:
        print(f"Error adding API to collection: {e}")

# Test the APIs by sending requests and printing the response
for api in api_list:
    try:
        response = requests.request(
            api["request"]["method"], api["request"]["url"], json=api["request"].get("body", {})
        )
        print(f"API: {api['name']}")
        print(f"Status code: {response.status_code}")
        print(f"Response body: {response.text}")
    except Exception as e:
        print(f"Error testing API: {e}")

# Save the results of the tests to a JSON file
results = []
for api in api_list:
    result = {
        "name": api["name"],
        "status_code": response.status_code,
        "response_body": response.text
    }
    results.append(result)

with open("results.json", "w") as f:
    json.dump(results, f)
