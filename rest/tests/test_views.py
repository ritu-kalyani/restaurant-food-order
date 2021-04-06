from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Product, Contact, Orders, OrderUpdate
import json

class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('ShopHome')
        self.about_url = reverse('AboutUs')
        self.contact_url = reverse('ContactUs')
        self.tempProduct = Product.objects.create(
            id=5,
            product_name='Temp',
            category='TempCategory',
            price=400,
            desc='Temp Description',
        )
        self.tempOrder = Orders.objects.create(
            order_id=5,
            items_json='{}',
            name='TempName',
            email='temp@gmail.com',
            address='Temp',
            city='Temp',
            state='Temp',
            zip_code='temp',
            phone='4521234523'
        )
        self.product_id_url = reverse('ProductView', args=[5])
        self.tracker_url = reverse('TrackingStatus')
        self.search_url = reverse('search')
        self.checkout_url = reverse('Checkout')
        self.faq_url = reverse('faq')

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index2.html')

    def test_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contact_GET(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_product_id_GET(self):
        response = self.client.get(self.product_id_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'prodview.html')
  
    def test_tracker_GET(self):
        response = self.client.post(self.tracker_url, {'orderId': 5, 'email': 'temp@gmail.com'})
        self.assertEquals(response.status_code, 200)
        order = Orders.objects.get(order_id=5, email='temp@gmail.com')
        self.assertEquals(order.email, 'temp@gmail.com')
        self.assertEquals(order.order_id, 5)
        self.assertTemplateUsed(self.client.get(self.tracker_url), 'tracker.html')

    def test_faq_GET(self):
        response = self.client.get(self.faq_url)
        self.assertTemplateUsed(response, 'faq.html')

    def test_contact_GET(self):
        response = self.client.post(self.contact_url, { 'name': 'Temp', 'email': 'temp@gmail.com', 'phone':'4521234523', "desc": 'Temp Description' })
        self.assertTemplateUsed(self.client.get(self.contact_url), 'contact.html')
    

