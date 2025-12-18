from django.urls import path
from . import views

# localhost:8000/blog
#localhost:8000/blog/writers
urlpatterns = [
    path('',views.all_products,name='blog_home'),
    path('writers/', views.writersList),
    
]
