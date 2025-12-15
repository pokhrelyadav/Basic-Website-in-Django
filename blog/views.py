from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_blog(req):
    return render(req, 'blog/myblog.html')

def writersList(req):
    return HttpResponse("Writer: Yadav Pokhrel")