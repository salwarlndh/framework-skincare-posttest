from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib import messages
from .forms import ProductForm
from django.http import JsonResponse
from django.db.models import Q

def homepage(request):
    return render(request, 'homepage/home.html')

def about(request):
    return render(request, 'homepage/about.html')

def product(request):
    return render(request, 'homepage/product.html')

# READ Product
def product_index(request):
    product = Product.objects.all()
    return render(request, 'product/index.html', {'product': product})

def product_index2(request):
    product = Product.objects.all()
    return render(request, 'homepage/product.html', {'product': product})


# CREATE Product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save() # Simpan data product ke database
            messages.success(request, 'Product Created') # Pesan sukses
            return redirect('product_index') # Redirect ke halaman index product
    else:
        form = ProductForm()
    return render(request, 'product/create.html', {'form': form})

# UPDATE Product
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated')
            return redirect('product_index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/update.html', {'form': form, 'product': product})

# DELETE Product
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product Deleted')
    return JsonResponse({'success': True})

# Search Product
def product_index(request):
    query = request.GET.get('q')
    product = Product.objects.all()
    if query:
        product = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(stock__icontains=query)
        )
    else:
        product = Product.objects.all()
    return render(request, 'product/index.html', {'product': product, 'query': query})

def product_index2(request):
    query = request.GET.get('q')
    product = Product.objects.all()
    if query:
        product = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(stock__icontains=query)
        )
    else:
        product = Product.objects.all()
    return render(request, 'homepage/product.html', {'product': product, 'query': query})