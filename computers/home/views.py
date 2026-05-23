from django.shortcuts import render, redirect
from .models import Computer

def home(request):
    return render(request, 'index.html')

def laptops(request):
    laptops = Computer.objects.all()
    return render(request, 'laptops.html', {'laptops': laptops})

def add(request):
    if request.method == 'POST':
        
        model = request.POST.get('model')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        color = request.POST.get('color')
        screen_size = request.POST.get('screen_size')
        features = request.POST.get('features')
        image = request.FILES.get('image')
        if not image:
            Computer.objects.create(model=model, brand=brand, color=color, screen_size=screen_size, features=features, price=price)
        else:
            Computer.objects.create(model=model, brand=brand, color=color, screen_size=screen_size, features=features, price=price, image=image)
        
        return redirect('explore')
    
    return render(request, 'add.html')

def detail(request, pk):
    laptop = Computer.objects.filter(id=pk).first()
    
    return render(request, 'detailed.html', {'laptop': laptop})
