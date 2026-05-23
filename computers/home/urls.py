from django.urls import path
from .views import home, laptops, add


urlpatterns = [
    path('', home, name='home'),
    path('explore', laptops, name='explore'),
    path('add', add, name='add')
]