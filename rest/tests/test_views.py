from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Product, Contact, Orders, OrderUpdate, UserData
import json
import sqlite3

class TestView(TestCase):
    def setUp(self):
        self.tempProduct = Product.objects.create(
            id=5,
            product_name='Temp',
            category='TempCategory',
            price=400,
            desc='Temp Description',
        )
        self.user = UserData.objects.create(
            username='parthKalbag',
            fullname='Parth',
            email='temp@gmail.com',
            address='temp Address',
            city='temp city',
            state='temp state',
            zip_code='temp zip',
            phone='temp phone'
        )
        self.client = Client()
        self.index_url = reverse('ShopHome')
        self.about_url = reverse('AboutUs')
        self.contact_url = reverse('ContactUs')
        self.product_id_url = reverse('ProductView', args=[5])
        self.tracker_url = reverse('TrackingStatus')
        self.search_url = reverse('search')
        self.checkout_url = reverse('Checkout')
        self.faq_url = reverse('faq')
        self.register_url=reverse('Register')
        self.login_url = reverse('Login')

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index2.html')

    def test_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    
    def test_product_id_GET(self):
        response = self.client.get(self.product_id_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'prodview.html')

    def test_register_valid_POST(self):
        response = self.client.post(self.register_url, {'username': 'Temp Username', 'full-name': 'Temp Full Name', 'email-address': 'temp@gmail.com', 'present_address': 'Temp Address', 'city': 'Temp City', 'state': 'Temp State', 'zip': 'Temp zip', 'phone_number': 'Phone No', 'full-password': 'tempPass'})
        self.assertEquals(response.status_code, 200)

    def test_register_invalid_POST(self):
        self.test_register_valid_POST()
        # Check using invalid credentials
        false = self.client.post(self.register_url, {'username': 'Temp Username', 'full-name': 'Temp Full Name', 'email-address': 'temp@gmail.com', 'present_address': 'Temp Address', 'city': 'Temp City', 'state': 'Temp State', 'zip': 'Temp zip', 'phone_number': 'Phone No', 'full-password': 'tempPass'})
        self.assertEquals(false.status_code, 409)
       

    def test_login_POST(self):
        # Check using valid credentials
        self.test_register_valid_POST()
        response = self.client.post(self.login_url, {'username': 'Temp Username', 'password': 'tempPass'})
        self.assertEquals(response.status_code, 302)

        # Check using invalid credentials
        false_creds = self.client.post(self.login_url, {'username': 'Temp Username', 'password': 'tempPass234'})
        self.assertEquals(false_creds.status_code, 401)

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        
    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')