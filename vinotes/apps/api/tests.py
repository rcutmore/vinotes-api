from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Wine, Winery


def add_user(username, email):
    """
    Create and return a new user with the given username and email.
    """
    user = User.objects.create_user(
        username=username, email=email, password='test')
    user.save()
    return user


def add_wine(winery, name, vintage):
    """
    Create and return a new wine with the given name.
    """
    return Wine.objects.create(winery=winery, name=name, vintage=vintage)


def add_winery(name):
    """
    Create and return a new winery with the given name.
    """
    return Winery.objects.create(name=name)


class NoteTests(APITestCase):
    def setUp(self):
        add_user('test', 'test@test.com')
        winery = add_winery('test')
        add_wine(winery, 'test', 2015)


    def test_create_note_with_authentication(self):
        """
        Ensure that we can create a new note after logging in.
        """
        self.client.login(username='test', password='test')

        # Send POST request to create note.
        url = reverse('note-list')
        wine_url = reverse('wine-detail', kwargs={'pk': 1})
        data = {'wine': wine_url, 'tasted': datetime.now(),'rating': 5}
        response = self.client.post(url, data, format='json')

        # Make sure note was created with expected data.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_tasted = datetime.strptime(
            response.data['tasted'], '%Y-%m-%dT%H:%M:%S.%fZ')
        self.assertEqual(response_tasted.date(), data['tasted'].date())
        self.assertEqual(response.data['rating'], data['rating'])
        new_note_url = reverse('note-detail', kwargs={'pk': 1})
        self.assertTrue(new_note_url in response.data['url'])


    def test_create_note_without_authentication(self):
        """
        Ensure that we cannot create a new note without logging in.
        """
        # Send POST request to create note.
        url = reverse('note-list')
        wine_url = reverse('wine-detail', kwargs={'pk': 1})
        data = {'wine': wine_url, 'rating': 5}
        response = self.client.post(url, data, format='json')

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('taster' not in response.data)
        self.assertTrue('tasted' not in response.data)
        self.assertTrue('rating' not in response.data)


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
        Ensure that we cannot create a new trait without logging in.
        """
        # Send POST request to create trait.
        url = reverse('trait-list')
        data = {'name': 'test'}
        response = self.client.post(url, data, format='json')

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('name' not in response.data)


class WineTests(APITestCase):
    def setUp(self):
        add_user('test', 'test@test.com')
        add_winery('test')


    def test_create_wine_with_authentication(self):
        """
        Ensure that we can create a new wine after logging in.
        """
        self.client.login(username='test', password='test')

        # Send POST request to create wine.
        url = reverse('wine-list')
        winery_url = reverse('winery-detail', kwargs={'pk': 1})
        data = {'winery': winery_url, 'name': 'test', 'vintage': 2015}
        response = self.client.post(url, data, format='json')

        # Make sure wine was created with expected data.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(data['winery'] in response.data['winery'])
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['vintage'], data['vintage'])
        new_wine_url = reverse('wine-detail', kwargs={'pk': 1})
        self.assertTrue(new_wine_url in response.data['url'])


    def test_create_wine_without_authentication(self):
        """
        Ensure that we cannot create a new wine without logging in.
        """
        # Send POST request to create wine.
        url = reverse('wine-list')
        winery_url = reverse('winery-detail', kwargs={'pk': 1})
        data = {'winery': winery_url, 'name': 'test', 'vintage': 2015}
        response = self.client.post(url, data, format='json')

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('winery' not in response.data)
        self.assertTrue('name' not in response.data)
        self.assertTrue('vintage' not in response.data)


class WineryTests(APITestCase):
    def setUp(self):
        add_user('test', 'test@test.com')


    def test_create_winery_with_authentication(self):
        """
        Ensure that we can create a new winery after logging in.
        """
        self.client.login(username='test', password='test')

        # Send POST request to create winery.
        url = reverse('winery-list')
        data = {'name': 'test'}
        response = self.client.post(url, data, format='json')

        # Make sure winery was created with expected data.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        new_winery_url = reverse('winery-detail', kwargs={'pk': 1})
        self.assertTrue(new_winery_url in response.data['url'])


    def test_create_winery_without_authentication(self):
        """
        Ensure that we cannot create a new winery without logging in.
        """
        # Send POST request to create winery.
        url = reverse('winery-list')
        data = {'name': 'test'}
        response = self.client.post(url, data, format='json')

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('name' not in response.data)