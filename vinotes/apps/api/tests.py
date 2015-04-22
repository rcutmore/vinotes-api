from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Wine, Winery


def add_user(username='test', email='test@test.com', password='test'):
    """
    Create and return a new user with the given username and email.
    """
    user = User.objects.create_user(
        username=username, email=email, password=password)
    user.save()
    return user


def add_wine(winery, name='test', vintage=2015):
    """
    Create and return a new wine with the given winery, name, and vintage.
    """
    return Wine.objects.create(winery=winery, name=name, vintage=vintage)


def add_winery(name='test'):
    """
    Create and return a new winery with the given name.
    """
    return Winery.objects.create(name=name)


class NoteTests(APITestCase):
    def setUp(self):
        add_user()
        winery = add_winery()
        add_wine(winery)


    def send_post_request(self):
        """
        Send POST request to create note and return data and response.
        """
        url = reverse('note-list')
        wine_url = reverse('wine-detail', kwargs={'pk': 1})

        data = {'wine': wine_url, 'tasted': datetime.now(),'rating': 5}
        response = self.client.post(url, data, format='json')
        
        return (data, response)


    def test_create_note_with_authentication(self):
        """
        Ensure that we can create a new note after logging in.
        """
        self.client.login(username='test', password='test')

        data, response = self.send_post_request()

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
        data, response = self.send_post_request()

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('taster' not in response.data)
        self.assertTrue('tasted' not in response.data)
        self.assertTrue('rating' not in response.data)


class TraitTests(APITestCase):
    def setUp(self):
        add_user()


    def send_post_request(self):
        """
        Send POST request to create trait and return data and response.
        """
        url = reverse('trait-list')

        data = {'name': 'test'}
        response = self.client.post(url, data, format='json')

        return (data, response)


    def test_create_trait_with_authentication(self):
        """
        Ensure that we can create a new trait after logging in.
        """
        self.client.login(username='test', password='test')

        data, response = self.send_post_request()

        # Make sure trait was created with expected data.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        new_trait_url = reverse('trait-detail', kwargs={'pk': 1})
        self.assertTrue(new_trait_url in response.data['url'])


    def test_create_trait_without_authentication(self):
        """
        Ensure that we cannot create a new trait without logging in.
        """
        data, response = self.send_post_request()

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('name' not in response.data)


class WineTests(APITestCase):
    def setUp(self):
        add_user()
        add_winery()


    def send_post_request(self):
        """
        Send POST request to create wine and return data and response.
        """
        url = reverse('wine-list')
        winery_url = reverse('winery-detail', kwargs={'pk': 1})

        data = {'winery': winery_url, 'name': 'test', 'vintage': 2015}
        response = self.client.post(url, data, format='json')

        return (data, response)


    def test_create_wine_with_authentication(self):
        """
        Ensure that we can create a new wine after logging in.
        """
        self.client.login(username='test', password='test')

        data, response = self.send_post_request()

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
        data, response = self.send_post_request()

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('winery' not in response.data)
        self.assertTrue('name' not in response.data)
        self.assertTrue('vintage' not in response.data)


class WineryTests(APITestCase):
    def setUp(self):
        add_user()


    def send_post_request(self):
        """
        Send POST request to create winery and return data and response.
        """
        url = reverse('winery-list')

        data = {'name': 'test'}
        response = self.client.post(url, data, format='json')

        return (data, response)


    def test_create_winery_with_authentication(self):
        """
        Ensure that we can create a new winery after logging in.
        """
        self.client.login(username='test', password='test')

        data, response = self.send_post_request()

        # Make sure winery was created with expected data.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        new_winery_url = reverse('winery-detail', kwargs={'pk': 1})
        self.assertTrue(new_winery_url in response.data['url'])


    def test_create_winery_without_authentication(self):
        """
        Ensure that we cannot create a new winery without logging in.
        """
        data, response = self.send_post_request()

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('name' not in response.data)


    def test_view_winery_details_while_authenticated(self):
        """
        Ensure that we can view winery details while authenticated.
        """
        add_winery()
        self.client.login(username='test', password='test')

        # Send GET request for winery details.
        url = reverse('winery-detail', kwargs={'pk': 1})
        response = self.client.get(url)

        # Make sure correct winery details were returned.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'test')
        self.assertTrue(url in response.data['url'])


    def test_view_winery_details_while_unauthenticated(self):
        """
        Ensure that we cannot view winery details without authenticating.
        """
        add_winery()

        # Send GET request for winery details.
        url = reverse('winery-detail', kwargs={'pk': 1})
        response = self.client.get(url)

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('name' not in response.data)


class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure that we can create a user.
        """
        # Send POST request to create user.
        url = reverse('user-list')
        data = {'username': 'test', 'email': 'test@test.com', 'password': 'test'}
        response = self.client.post(url, data, format='json')

        # Make sure user was created.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])


    def test_view_user_details_while_authenticated_for_same_user(self):
        """
        Ensure that we can view user details while authenticated for same user.
        """
        add_user()
        self.client.login(username='test', password='test')

        # Send GET request for user details.
        url = reverse('user-detail', kwargs={'pk': 1})
        response = self.client.get(url)

        # Make sure correct user details are returned.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'test')
        self.assertEqual(response.data['email'], 'test@test.com')
        self.assertEqual(response.data['notes'], [])
        self.assertTrue(url in response.data['url'])


    def test_view_user_details_while_authenticated_for_different_user(self):
        """
        Ensure that we cannot view user details while authenticated for 
        different user.
        """
        add_user()
        add_user('test2', 'test2@test.com')
        self.client.login(username='test', password='test')

        # Send GET request for user details.
        url = reverse('user-detail', kwargs={'pk': 2})
        response = self.client.get(url)

        # Make sure 'not found' error was returned.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('username' not in response.data)
        self.assertTrue('email' not in response.data)
        self.assertTrue('notes' not in response.data)


    def test_view_user_details_while_unauthenticated(self):
        """
        Ensure that we cannot view user details without authenticating.
        """
        add_user()

        # Send GET request for user details.
        url = reverse('user-detail', kwargs={'pk': 1})
        response = self.client.get(url)

        # Make sure authentication error was returned.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('username' not in response.data)
        self.assertTrue('email' not in response.data)
        self.assertTrue('notes' not in response.data)