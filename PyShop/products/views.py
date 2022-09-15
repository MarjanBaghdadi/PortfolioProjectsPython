from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.


# /products --> index
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('Hello from inside the new folder')