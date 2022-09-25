from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import Post


# Create your views here.
def index(request):
    #return HttpResponse("this is home pg")
   # messages.success(request,"test msg")
    return render(request, 'index.html')
    

def about(request):
    #return HttpResponse("this is about pg")
    return render(request, 'about.html')

def learn(request):
    allPosts= Post.objects.all()
   # print(allPosts)
    context={'allPosts': allPosts}
    #return HttpResponse("this is blogs pg")
    return render(request, 'blogs.html',context)


def contact(request):
    #return HttpResponse("this is contact pg")
    
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        # datetime.today()
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Submitted!')
    return render(request, 'contact.html')

        

def price(request):
    #return HttpResponse("this is contact pg")


    return render(request, 'price.html')