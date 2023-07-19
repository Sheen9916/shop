from django.shortcuts import render
from django.http import HttpResponse
from.models import Product
# Create your views here.
def index(request):
    Products = Product.objects.all()
    return render(request,'index.html',{'products':Products})
 # return HttpResponse("<h1>welcome to django</h1>")


   

def about(request):
    return HttpResponse("<h1>about page</h1>")

def contact(request):
    return HttpResponse("<h1>contact page</h2>")