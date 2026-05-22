from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=400)
    photo = models.ImageField(upload_to='books', default='book_default.png', blank=True)
    author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    
