import unittest
import os
import json
from mock import Mock, patch

# Import the code that you want to test
import api_testing

class TestAPI(unittest.TestCase):
    def setUp(self):
        # Define the mock responses for the PostmanAPI and requests libraries
        self.mock_collection_response = {
            "id": "123",
            "name": "My Collection",
            "timestamp": 1623456789
        }
        self.mock_request_response = Mock()
        self.mock_request_response.status_code = 200
        self.mock_request_response.text = "OK"

        # Create a mock JSON file with the APIs
        api_list = [
            {
                "name": "API 1",
                "request": {
                    "method": "GET",
                    "url": "https://api.example.com/endpoint1"
                }
            },
            {
                "name": "API 2",
                "request": {
                    "method": "POST",
                    "url": "https://api.example.com/endpoint2",
                    "body": {
                        "mode": "raw",
                        "raw": "{\"key\":\"value\"}"
                    }
                }
            }
        ]
        with open("apis.json", "w") as f:
            json.dump(api_list, f)

    def tearDown(self):
        # Delete the mock JSON file with the APIs
        if os.path.exists("apis.json"):
            os.remove("apis.json")

        # Delete the mock JSON file with the results
        if os.path.exists("results.json"):
            os.remove("results.json")

    @patch("api_testing.PostmanAPI")
    @patch("api_testing.requests")
    def test_api_testing(self, mock_requests, mock_postman_api):
        # Set up the mock responses for the PostmanAPI and requests libraries
        mock_postman_api.return_value.collections.create.return_value = self.mock_collection_response
        mock_postman_api.return_value.requests.create.return_value = None
        mock_requests.request.return_value = self.mock
