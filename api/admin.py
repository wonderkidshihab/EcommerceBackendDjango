from django.contrib import admin
from product.models import Product, Category, SubCategory, ProductImage
# Register your models here.
admin.register(Product)
admin.register(Category)
admin.register(SubCategory)
admin.register(ProductImage)
