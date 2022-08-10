import re
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'index.html')
def about(request):
    return render(request ,'about.html')
def contact(request):
    return render(request ,'contact.html')
def products(request):
    return render(request ,'products.html')
def services(request):
    return render(request ,'services.html')
def gallery(request):
    return render(request ,'gallery.html')
