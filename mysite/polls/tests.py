from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.http import HttpRequest
from django.template import loader
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .models import ListItem
from .forms import ListItemForm
from django.test import TestCase, RequestFactory
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your tests here.
from .views import index

class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/index.html')

from .views import scrap


from .views import scrap

class ScrapTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_scrap(self):
        request = self.factory.post('/scrap/', {'ville': 'bretagne', 'minDistance': '10', 'maxDistance': '20'})
        response = scrap(request)

        self.assertIsInstance(response, list)

        expected_keys = ['title', 'city', 'img_url']
        for data in response:
            self.assertCountEqual(expected_keys, data.keys())

from .views import signup_view

class SignupViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_signup_view(self):
        request = self.factory.post('/signup/', {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        response = signup_view(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/polls/login/')  

