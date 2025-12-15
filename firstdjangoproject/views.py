from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is <b style='color:red;font-size:40px'>home</b> page")
    return render(request, 'website/index.html')

def about(request):
    print("-------Just Printing content of request ------")
    print("REQUEST OBJECT:", request)
    print("METHOD:", request.method)
    print("PATH: ", request.path)
    print("For home the path is /")
    print("SCHEME:", request.scheme)
    print("USER-AGENT:", request.headers.get("User-Agent"))
    print("AUTHORIZATION:", request.headers.get("Authorization"))
    print("USER:", request.user)
    print("CONTENT TYPE:", request.content_type)
    print("BODY:", request.body)
    print("--------End-----------")
    
    # return HttpResponse("This is <b style='color:red;font-size:40px'>about</b> page")
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')
