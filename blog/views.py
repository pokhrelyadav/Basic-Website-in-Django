from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def get_products(req):
    products = Product.objects.all()
    # print(type(products))
    return render(req, 'blog/myblog.html', {'allProductList': products})

def get_electronics(req):
    # return HttpResponse("Writer: Yadav Pokhrel")
    electronic_product = Product.objects.all()
    return render(req, 'blog/electronics.html', {'allElectronicsList':electronic_product})

def product_detail(req, product_id):
    oneProduct = get_object_or_404(Product, pk=product_id) # pk or id = same
    return render(req,'blog/productDetail.html' , {'oneProduct':oneProduct})