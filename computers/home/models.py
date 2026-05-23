from django.db import models

class Computer(models.Model):
    COLORS = (
        ('gray', 'Red',),
        ('black', 'Black'),
        ('cream', 'Cream'),
        ('navy', 'Navy'),
        ('white', 'White')
    )
    S_SIZE = (
        ('11.6', '11.6',),
        ('12', '12'),
        ('13.3', '13.3'),
        ('14', '14'),
        ('15.6', '15.6'),
        ('16', '16'),
        ('17.3', '17.3'),        
    )
    
    model = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=15, choices=COLORS)
    screen_size = models.CharField(max_length=5, choices=S_SIZE)
    features = models.CharField(max_length=500)
    image = models.ImageField(upload_to='computers/', default='default_computer.jpg', blank=True)
    
    def __str__(self):
        return self.model