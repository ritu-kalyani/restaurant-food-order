from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Product, Contact, Orders, OrderUpdate, UserData
import json

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