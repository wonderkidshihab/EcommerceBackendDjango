from django.db import models

# An ecommerce product related models
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.ImageField(upload_to='icons', blank=True, null=True)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
        
class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.ImageField(upload_to='icons', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Sub Categories"
        
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='product/thumbnail', null=True, blank=True)
    images = models.ManyToManyField('ProductImage', blank=True)
    
    def __str__(self):
        return self.name

    def get_price(self):
        return self.price - (self.price * self.discount/100)

    def get_discount(self):
        return self.price * self.discount/100

    def get_total_price(self):
        return self.price - self.get_discount()

    def get_total_discount(self):
        return self.get_discount() * self.quantity

    def get_total_price_with_discount(self):
        return self.get_total_price() * self.quantity

    class Meta:
        verbose_name_plural = "Products"
        

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product/images')

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name_plural = "Product Images"