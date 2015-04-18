from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


def add_user(username, email):
    """
    Create and return a new user with the given username and email.
    """
    user = User.objects.create_user(
        username=username, email=email, password='test')
    user.save()
    return user


class TraitTests(APITestCase):
    def setUp(self):
        add_user('test', 'test@test.com')


    def test_create_trait_with_authentication(self):
        """
        Ensure that we can create a new trait after logging in.
        """
        self.client.login(username='test', password='test')

        # Send POST request to create trait.
        url = reverse('trait-list')
        data = {'name': 'test'}
        response = self.client.post(url, data, format='json')

        # Make sure trait was created with expected data.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        new_trait_url = reverse('trait-detail', kwargs={'pk': 1})
        self.assertTrue(new_trait_url in response.data['url'])

    def test_create_trait_without_authentication(self):
        """
        Ensure that we cannot create a new trait without loggin in.
        """
        # Send POST request to create trait.
        url = reverse('trait-list')
        data = {'name': 'test'}
        response = self.client.post(url, data, format='json')

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('name' not in response.data)