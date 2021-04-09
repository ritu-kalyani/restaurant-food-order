from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import *

class TestUrls(SimpleTestCase):
    def test_index_is_resolved(self):
        url = reverse('ShopHome')
        self.assertEquals(resolve(url).func, index)
        
    def test_about_is_resolved(self):
        url = reverse('AboutUs')
        self.assertEquals(resolve(url).func, about)

    def test_contact_is_resolved(self):
        url = reverse('ContactUs')
        self.assertEquals(resolve(url).func, contact)
        
    def test_tracker_is_resolved(self):
        url = reverse('TrackingStatus')
        self.assertEquals(resolve(url).func, tracker)   
     
    def test_search_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    def test_product_id_is_resolved(self):
        url = reverse('ProductView', args=[5])
        self.assertEquals(resolve(url).func, productview)
        
    def test_checkout_is_resolved(self):
        url = reverse('Checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_faq_is_resolved(self):
        url = reverse('faq')
        self.assertEquals(resolve(url).func, faq)

    def test_register_is_resolved(self):
        url = reverse('Register')
        self.assertEquals(resolve(url).func, register)

    def test_login_is_resolved(self):
        url = reverse('Login')
        self.assertEquals(resolve(url).func, login)

    def test_logout_is_resolved(self):
        url = reverse('Logout')
        self.assertEquals(resolve(url).func, logout)

    