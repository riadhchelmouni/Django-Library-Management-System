from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
    
    # Render the page with form and data
    context = {
        'categories': Category.objects.all(),
        'books': Book.objects.all(),
        'form': BookForm(),
        'formcat': CategoryForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'booksold': Book.objects.filter(status='sold').count(),
        'bookrental': Book.objects.filter(status='rented').count(),
        'bookavailable': Book.objects.filter(status='available').count(),
    }
    return render(request, 'pages/index.html', context)
def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    
    
    context = {
        'categories': Category.objects.all(),
        'books': search,
    }
    return render(request, 'pages/books.html', context) 


def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        update_book = BookForm(request.POST, request.FILES, instance=book_id)
        if update_book.is_valid():
            update_book.save()
            return redirect('index')
    else:
        update_book = BookForm(instance=book_id)
    context = {
        'form': update_book,
    }
    return render(request, 'pages/update.html', context)


def delete(request, id):
    book_detele = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_detele.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')