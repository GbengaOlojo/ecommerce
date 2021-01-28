from django.urls import path
from .views import index, get_product

urlpatterns = [
    path('', index, name="index"),
    path('products', get_product, name='products')

]