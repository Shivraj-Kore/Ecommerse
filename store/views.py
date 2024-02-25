from django.shortcuts import render
# from django.http import HttpResponse
from .models import *

def home(request):
    context = {}
    return render(request , 'index.html' , context)

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request , 'store.html' , context)

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , is_order_complete = False)
        
        #this is short for     ||
        #                      V
        # try:
        #     order = Order.objects.get()
        # except Order.DoesNotExist:
        #     order = Order.objects.create()

        items = order.orderitems_set.all()
    else:
        items = []

    context = {'items':items}
    return render(request , 'cart.html' , context)

def checkout(request):
    context = {}
    return render(request , 'checkout.html' , context)