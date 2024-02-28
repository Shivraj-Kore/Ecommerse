from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json


def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , is_order_complete = False)
        total_cart_items = order.get_cart_total_items
    else:
        order = {'get_cart_total_items':0 , 'get_cart_total_price':0}
        total_cart_items = order['get_cart_total_items']
    context = {'total_cart_items':total_cart_items}
    return render(request , 'index.html' , context)

def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , is_order_complete = False)
        total_cart_items = order.get_cart_total_items
    else:
        order = {'get_cart_total_items':0 , 'get_cart_total_price':0}
        total_cart_items = order['get_cart_total_items']

    products = Product.objects.all()
    context = {'products':products , 'total_cart_items':total_cart_items}
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
        total_cart_items = order.get_cart_total_items

    else:
        items = []
        order = {'get_cart_total_items':0 , 'get_cart_total_price':0}
        total_cart_items = order['get_cart_total_items']

    context = {'items':items , 'order':order , 'total_cart_items':total_cart_items}
    return render(request , 'cart.html' , context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , is_order_complete = False)
        items = order.orderitems_set.all()
        total_cart_items = order.get_cart_total_items
    else:
        items = []
        order = {'get_cart_total_items':0 , 'get_cart_total_price':0}
        total_cart_items = order['get_cart_total_items']

    context = {'items':items , 'order':order , 'total_cart_items':total_cart_items }
    return render(request , 'checkout.html' , context)

# add item to cart
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    # print(action , productId)
    customer = request.user.customer
    product = Product.objects.get(id = productId)

    order , created = Order.objects.get_or_create(customer = customer , is_order_complete = False)

    orderItem , created = OrderItems.objects.get_or_create(order=order , product=product)

    if action == 'add' :
        orderItem.quantity=(orderItem.quantity + 1)
    elif action == 'remove' :
        orderItem.quantity = (orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <= 0 :
        orderItem.delete()

    return JsonResponse("Item was added yaaaaaaaaaaaaay" , safe = False)