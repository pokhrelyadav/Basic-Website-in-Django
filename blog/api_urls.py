from . import api
from django.urls import path

urlpatterns=[
    path('all-products/', api.product_list_api,name='get_allproduct_api'),
]