from django.test import TestCase
from django.urls import reverse

from .models import User


class RegistrationTest(TestCase):

    def test_register_page(self):
        response = self.client.get(
            reverse('accounts:register')
        )

        self.assertEqual(response.status_code, 200)


def test_login(self):

    User.objects.create_user(
        username='testuser',
        password='StrongPassword123'
    )

    response = self.client.post(
        reverse('accounts:login'),
        {
            'username': 'testuser',
            'password': 'StrongPassword123',
        }
    )

    self.assertEqual(response.status_code, 302)


def test_students_requires_login(self):

    response = self.client.get(
        reverse('main:student-list')
    )

    self.assertEqual(response.status_code, 302)