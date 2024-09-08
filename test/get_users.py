import requests
from config.config import config
from endpoint.endpoint import endpoint

class TestGetUser:
    def test_get_users(self):
        # Define the URL of the API endpoint
        base_url = config.base_url

        # Send a GET request to the API
        url= base_url+ endpoint.get_user

        response = requests.get(url)

        # Check if the request was successful (status code 200)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        # Parse the response JSON
        response = response.json()

        # Expected keys at the top level of the response
        expected_keys = {"page", "per_page", "total", "total_pages", "data", "support"}

        # Assert that all expected keys are present in the response
        assert all(key in response for key in expected_keys), "Response is missing some expected top-level keys"

        # Expected keys for each user in the 'data' list
        expected_user_keys = {"id", "email", "first_name", "last_name", "avatar"}

        # Assert that each user in the 'data' list has the expected keys
        for user in response['data']:
            assert all(key in user for key in expected_user_keys), f"User data is missing some expected keys: {user}"

        # Expected keys for the 'support' object
        expected_support_keys = {"url", "text"}

        # Assert that 'support' object has the expected keys
        assert all(key in response['support'] for key in
                   expected_support_keys), "Support object is missing some expected keys"

        # Print the users for verification
        print("All keys are present and users retrieved successfully:", response)

        # Print the list of users for verification
        print("Users retrieved successfully:", response)
