from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    context = {
        'categories': Category.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'pages/index.html', context)  

def books(request):
    context = {
        'categories': Category.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'pages/books.html', context) 