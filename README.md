# Postman-automation
This script automate checking the APIs list of a user and handle errors

#### This code does the following:

- Imports the necessary libraries: `os`, `json`,` postman_api`, and `requests`
<!--more-->


- Initializes the `PostmanAPI` object with your API key
<!--more-->


- Defines an empty list of APIs that you want to add to Postman
<!--more-->


- Reads the APIs from a JSON file (`apis.json`) and stores them in the `api_list` variable
<!--more-->


- Creates a Postman collection to store the APIs, with error handling to catch any exceptions that might occur
<!--more-->


- Adds the APIs to the collection, with error handling to catch any exceptions that might occur
<!--more-->


- Tests the APIs by sending requests and printing the response, with error handling to catch any exceptions that might occur
<!--more-->


- Saves the results of the tests to a JSON file (`results.json`)
