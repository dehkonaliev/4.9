from django.urls import path
from .views import home, books_list, add_book, detailed

urlpatterns = [
    path('', home, name='home'),
    path('books/', books_list, name='book_list'),
    path('new-book/', add_book, name='new-book'),
    path('detailed/<int:pk>', detailed, name='detailed'),
]