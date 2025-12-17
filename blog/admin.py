from django.contrib import admin
#import Product model from models.py (module)
from .models import Product
# Register your models here.
admin.site.register(Product)