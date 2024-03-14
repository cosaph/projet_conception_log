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
        
## -----------------------------OK JUSQU'ICI-------------------------------- ##
        
from .views import logout_view

class LogoutViewTest(TestCase):
    def test_logout_view(self):
        request = HttpRequest()
        request.method = 'GET'
        user = User.objects.create_user(username='testuser', password='password123')  
        request.user = user
        login(request, user)  
        response = logout_view(request)

        self.assertFalse(request.user.is_authenticated)

        self.assertRedirects(response, reverse('index'))

from .views import list_view

class ListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_list_view_get(self):
        request = HttpRequest()
        request.method = 'GET'
        request.user = self.user

        response = list_view(request)

        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'list.html')  

    def test_list_view_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.user = self.user
        request.POST['item_name'] = 'Test Item'

        response = list_view(request)

        self.assertTrue(ListItem.objects.filter(user=self.user, item_name='Test Item').exists())

        self.assertRedirects(response, reverse('list'))

from .views import add_item

class AddItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_add_item_view_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.user = self.user
        request.POST['title'] = 'Test Title'
        request.POST['city'] = 'Test City'

        response = add_item(request)

        self.assertTrue(ListItem.objects.filter(user=self.user, content='Test Title, Test City').exists())

        self.assertTemplateUsed(response, 'list.html')

        self.assertEqual(response.context['title'], 'Test Title')
        self.assertEqual(response.context['city'], 'Test City')

    def test_add_item_view_get(self):
        request = HttpRequest()
        request.method = 'GET'

        response = add_item(request)

        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.content.decode('utf-8'), 'Invalid request')  


from .views import delete_item_view

class DeleteItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_delete_item_view(self):
        item = ListItem.objects.create(user=self.user, content="Test item content")

        request = HttpRequest()
        request.method = 'POST'
        request.user = self.user

        response = delete_item_view(request, item.id)

        self.assertFalse(ListItem.objects.filter(id=item.id).exists())

        self.assertRedirects(response, reverse('list'))

