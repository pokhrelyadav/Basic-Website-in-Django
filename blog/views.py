from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.
def all_products(req):
    products = Product.objects.all()
    print(type(products))
    return render(req, 'blog/myblog.html', {'allProductList': products})

def writersList(req):
    return HttpResponse("Writer: Yadav Pokhrel")