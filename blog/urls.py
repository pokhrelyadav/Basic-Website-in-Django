from django.urls import path
from . import views

# localhost:8000/blog
#localhost:8000/blog/writers
urlpatterns = [
    path('',views.get_products,name='blog_home'),
    path('electronics/', views.get_electronics,name='blog_electronics'),
    
    path('electronics/<int:product_id>/', views.product_detail, name='blog_productdetail'),
    
]
