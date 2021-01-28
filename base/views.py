from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(
        request,
        'index.html'
    )

def get_product(request):
    products = Product.objects.all()
    return JsonResponse({'data' : list(products)}, safe=False )



