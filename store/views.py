from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room


# Create your views here.



def home(request):
    context ={}
    return render (request,'store/home.html',context)
def store(request):
     products =Product.objects.all()
     context = {'products' : products}
     return render(request, 'store/store.html', context)

def cart(request):

     if request.user.is_authenticated:
        customer =request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
     else:
        items = [ ]
        order ={'get_cart_total':0, 'get_cart_items':0}


     context = {'items' : items, 'order':order}
     return render(request, 'store/cart.html', context)

def checkout(request):
      if request.user.is_authenticated:
        customer =request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
      else:
        items = [ ]
        order ={'get_cart_total':0, 'get_cart_items':0}


      context = {'items' : items, 'order':order}
      return render(request, 'store/checkout.html', context)

