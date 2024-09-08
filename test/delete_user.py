import requests
from config.config import config
from endpoint.endpoint import endpoint

class TestDeleteUser:
    def test_delete_user(self):
        # Define the URL of the API endpoint
        base_url = config.base_url

        url = base_url + endpoint.delete_user

        # Send a PUT request to the API
        response = requests.delete(url)

        # Check if the request was successful (status code 200 or 201 for successful creation/update)
        assert response.status_code == 204, f"Expected status code 200 or 201, but got {response.status_code}"

        print("User deleted successfully")