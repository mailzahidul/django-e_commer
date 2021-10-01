from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'product_list':products,
    }
    return render(request, 'home.html', context)