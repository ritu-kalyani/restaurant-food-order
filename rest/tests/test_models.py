from django.test import TestCase
from shop.models import Product, Contact, Orders, OrderUpdate

class TestModels(TestCase):
    def setUp(self):
        self.product = Product.objects.create(id=2,product_name='TempProduct', category='TempCategory', price=1000, desc='Temp Desc')
        self.contact = Contact.objects.create(msg_id=2,name='TempName', email='temp@gmail.com', phone='TempPhone', desc='TempDesc')
        self.order = Orders.objects.create(
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

    def checkIfModelsCreated(self):
        self.assertEquals(Product.objects.get(id=2), self.product)
        self.assertEquals(Contact.objects.get(msg_id=2), self.contact)
        self.assertEquals(Orders.objects.get(order_id=5), self.order)
