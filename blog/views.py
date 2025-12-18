from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.
def get_products(req):
    products = Product.objects.all()
    # print(type(products))
    return render(req, 'blog/myblog.html', {'allProductList': products})

def get_electronics(req):
    # return HttpResponse("Writer: Yadav Pokhrel")
    electronic_product = Product.objects.all()
    return render(req, 'blog/electronics.html', {'allElectronicsList':electronic_product})