from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User , null = False , blank=False , on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50)
    email= models.EmailField(null=False, max_length=200)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length = 100 , null = False)
    price = models.IntegerField(max_length = 10)
    image = models.ImageField(blank = True  , null = True)

    def __str__(self) :
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/images/noimg.jpg/'
        return url
    
class Order(models.Model):
    customer = models.ForeignKey(Customer , on_delete = models.SET_NULL , blank=True , null=True)
    date_of_order = models.DateTimeField(auto_now_add = True)
    is_order_complete = models.BooleanField(default = False , null = True , blank = False)
    transaction_id = models.CharField(max_length = 200 , null = True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total_price(self):
        order_items = self.orderitems_set.all()
        total = sum([item.get_total for item in order_items])
        return total
    
    @property
    def get_cart_total_items(self):
        order_items = self.orderitems_set.all()
        total = sum([item.quantity for item in order_items])
        return total

class OrderItems(models.Model):
    product = models.ForeignKey(Product , on_delete=models.SET_NULL , blank = True , null = True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL , blank = True , null = True)
    quantity = models.IntegerField(default = 0 , null = True , blank = True)
    date_added_item = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):

        total = self.product.price * self.quantity
        return total

class ShippingAddress (models.Model):
    customer = models.ForeignKey(Customer , on_delete = models.SET_NULL , blank = True , null = True)
    order = models.ForeignKey(Order , on_delete = models.SET_NULL , blank = True , null = True)
    address = models.CharField(max_length=200 , null = True)
    city = models.CharField(max_length = 200 , null = True)
    state = models.CharField(max_length = 200 , null = True)
    pincode = models.CharField(max_length=50 , null = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.city