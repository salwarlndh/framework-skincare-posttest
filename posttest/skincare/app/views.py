from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/home.html')

def about(request):
    return render(request, 'homepage/about.html')

def product(request):
    return render(request, 'homepage/product.html')