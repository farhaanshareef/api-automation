import requests
from config.config import config
from endpoint.endpoint import endpoint
class TestPatchUser:
    def test_patch_user(self):
        # Define the URL of the API endpoint
        base_url = config.base_url

        # Construct the full URL for the PUT request
        url = base_url + endpoint.put_user

        # Define the body for the PUT request
        body = {
            "name": "morpheus",
            "job": "zion resident"
        }

        # Send a PUT request to the API
        response = requests.patch(url, json=body)

        # Check if the request was successful (status code 200 or 201 for successful creation/update)
        assert response.status_code in [200, 201], f"Expected status code 200 or 201, but got {response.status_code}"

        # Parse the response JSON
        put_response = response.json()

        # Expected keys in the PUT response
        expected_put_keys = {"name", "job", "updatedAt"}

        # Assert that all expected keys are present in the PUT response
        assert all(key in put_response for key in expected_put_keys), f"PUT response is missing some expected keys: {put_response}"

        # Assert that the response contains the same 'name' and 'job' values as the request body
        assert put_response["name"] == body["name"], f"Expected name '{body['name']}', but got '{put_response['name']}'"
        assert put_response["job"] == body["job"], f"Expected job '{body['job']}', but got '{put_response['job']}'"

        # Print the PUT response for verification
        print("User updated successfully with response:", put_response)