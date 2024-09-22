import requests
from config.config import config
from endpoint.endpoint import endpoint

class TestCreateUser:
    def test_create_user(self):
        # Define the URL of the API endpoint
        base_url = config.base_url
        url = base_url + endpoint.post_user

        # Define the body for the POST request
        body = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

        # Send a POST request to the API
        response = requests.post(url, json=body)

        # Check if the request was successful (status code 201)
        assert response.status_code == 200, f"Expected status code 201, but got {response.status_code}"

        # Parse the response JSON
        post_response = response.json()

        # Expected keys in the POST response
        expected_post_keys = {"id", "token"}

        # Assert that all expected keys are present in the POST response
        assert all(key in post_response for key in expected_post_keys), f"POST response is missing some expected keys: {post_response}"
        print("User created successfully with response:", post_response)
