from django.urls import path
from .views import home, laptops, add, detail


urlpatterns = [
    path('', home, name='home'),
    path('explore', laptops, name='explore'),
    path('add', add, name='add'),
    path('detail/<int:pk>', detail, name='detail')
]