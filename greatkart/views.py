from django.shortcuts import render
from store.models import Product

def home(request):

    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    context = {
        'products': products,
    }
    
    return render(request, 'home.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }

    return render(request, 'store/product_detail.html', context)