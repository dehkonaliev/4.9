from django.shortcuts import render, redirect
from .models import Book

def home(request):
    
    return render(request, 'index.html')

def books_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        author = request.POST.get('author')
        price = request.POST.get('price')
        photo = request.FILES.get('photo')
        
        new_book = Book(
            title=title,
            summary=summary,
            author=author,
            price=price,
            photo=photo
        )
        
        new_book.save()
        
        return redirect('book_list')
    
    return render(request, 'add_book.html')

def detailed(request, pk):
    book = Book.objects.get(pk=pk)
    
    return render(request, 'detailed.html', {'book':book})