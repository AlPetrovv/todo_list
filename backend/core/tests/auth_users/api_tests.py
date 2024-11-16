import json
import os.path

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient, APITestCase

User = get_user_model()

url_registration: str = reverse(...)
url_login: str = reverse(...)
url_logout: str = reverse(...)

class BaseUserAuthAPI(APITestCase):
    """
    The class which tests every auth endpoints separately.
    This was done in order to be able to simply add the endpoints that are needed.
    """
    def _reg(self, data: dict):
        """
        The function that registers the user and checks the response.
        The data consists of email, password and re_password
        """
        response: Response = self.client.post(url_registration, data, follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        return response

    def _login(self, data: dict) -> Response:
        """
        The function that logins the user and checks the response.
        The data consists of email and password
        """
        response: Response = self.client.post(url_login, data, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        return response

    def _delete_user(self, url: str) -> Response:
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        return response

    def _logout(self, data: dict) -> Response:
        response = self.client.post(url_logout, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        return response


class UserAPITestCase(BaseUserAuthAPI, APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()


    def test_registration_201(self) -> None:
        """
        testing the registration endpoint with the right data
        """
        with open(os.path.join(os.path.dirname(__file__), "fixtures/users.json")) as fp:
            test_data = json.load(fp)

        for data in test_data:
            self._reg(data)