from django.contrib import admin

# Register your models here.
from .models import Product,Contact,Orders,OrderUpdate, User

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(User)