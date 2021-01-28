from django.db import models
from cloudinary.models import CloudinaryField


class Brand(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        

class Product(models.Model):
    CATEGORIES = (
    
        ('01', 'Spirits'),
        ('02', 'Wines'),
        ('03',  'Beers'),
        ('04', 'Gas carnisters'),
        ('05', 'Internationals'),
        ('06', 'Beverages/non alcoholic'),
        ('07', 'Others')
    )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    bva_volume = models.PositiveIntegerField()
    category = models.CharField(choices=CATEGORIES, max_length=20)
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

    def agregate(self, units):
        return self.price * units

    def check_availability(self):
        return self.available

    def update_quantity(self, no_of_items, update_type):
        if update_type == 'add':
            self.quantity += no_of_items
        else:
            self.quantity -= no_of_items
        return self.quantity
         

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = CloudinaryField('image')


    def __str__(self):
        return self.product.name 