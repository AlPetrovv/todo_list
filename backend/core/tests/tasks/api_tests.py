import json
import os

from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model

from apps.tasks.models import Task

User = get_user_model()

url_task_create: str = reverse('tasks:tasks-list')

class BaseTaskAPI(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def _delete_task(self, task_id: int) -> Response:
        url = reverse('tasks:tasks-detail', kwargs={'pk': task_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        return response

    def _create_task(self, data: dict) -> Response:
        response = self.client.post(url_task_create, data, follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        return response


    def _update_task(self, data: dict) -> Response:
        url = reverse('tasks:tasks-detail', kwargs={'pk': data['id']})
        response = self.client.patch(url, data, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        return response

class TaskAPITestCase(BaseTaskAPI):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(email='123@mail.com', password='0987poiu', id=1)
        self.client.force_authenticate(user=self.user)


    def test_create_task_201(self) -> None:
        """
        testing the login endpoint with the right data
        """

        with open(os.path.join(os.path.dirname(__file__), "fixtures/create_tasks_201.json")) as fp:
            test_data = json.load(fp)
        for data in test_data:
            self._create_task(data)

        self.assertEqual(Task.objects.count(), 3)


    def test_update_task_200(self) -> None:
        """
        testing the login endpoint with the right data
        """
        Task.objects.create(user=self.user, title='Task 1', description='Description 1', completed=False, id=1)
        Task.objects.create(user=self.user, title='Task 2', description='Description 2', completed=False, id=2)
        Task.objects.create(user=self.user, title='Task 3', description='Description 3', completed=False, id=3)

        with open(os.path.join(os.path.dirname(__file__), "fixtures/update_tasks_200.json")) as fp:
            test_data = json.load(fp)
        for data in test_data:
            self._update_task(data)

    def test_delete_task_204(self) -> None:
        """
        testing the login endpoint with the right data
        """
        Task.objects.create(user=self.user, title='Task 1', description='Description 1', completed=False, id=1)
        Task.objects.create(user=self.user, title='Task 2', description='Description 2', completed=False, id=2)
        Task.objects.create(user=self.user, title='Task 3', description='Description 3', completed=False, id=3)

        for tasks in Task.objects.all():
            self._delete_task(tasks.id)

        self.assertEqual(Task.objects.count(), 0)

