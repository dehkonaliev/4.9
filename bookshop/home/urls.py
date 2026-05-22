from django.urls import path
from .views import home, books_list, add_book

urlpatterns = [
    path('', home, name='home'),
    path('books/', books_list, name='book_list'),
    path('new-book/', add_book, name='new-book')
]