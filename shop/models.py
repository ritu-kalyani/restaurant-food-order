from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    # subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=int('100'),null=True)
    desc = models.CharField(max_length=3000)
    # pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=30,default="")
    desc=models.CharField(max_length=2000,default="")
   
    def __str__(self):
        return self.name        

class UserData(models.Model):
    username = models.CharField(max_length=255, primary_key=True, unique=True)
    fullname = models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, default="")

    def __str__(self):
        return f"{self.username}"

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, default="")
    user_id = models.ForeignKey(UserData, on_delete=models.DO_NOTHING, related_name="user_id")
    total = models.IntegerField(default=0)
    payment_id = models.CharField(max_length=200, default="")

    def __str__(self):
        return f"{self.name}"

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."      
   
