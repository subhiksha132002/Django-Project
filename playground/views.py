from django.shortcuts import render
from django.http import HttpResponse
from store.models  import Product,OrderItem

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    querset = Product.objects.values()
    return render(request,'hello.html',{'name':'Subhiksha'})


