from django.contrib import admin

# Register your models here.
from .models import Product,Contact,Orders,OrderUpdate, UserData
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(UserData)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)