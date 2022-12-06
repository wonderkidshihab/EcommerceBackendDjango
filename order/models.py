from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from product.models import Product

# Create your models here.


class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_product_price(self):
        return self.quantity * self.product.price

    def get_amount_saved(self):
        return self.get_total_product_price() - self.get_final_price()

    def get_final_price(self):
        return self.get_total_product_price()

    def get_absolute_url(self):
        return reverse("order:order-summary")


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for cart_product in self.products.all():
            total += cart_product.get_final_price()
        return total

    def get_total_quantity(self):
        total = 0
        for cart_product in self.products.all():
            total += cart_product.quantity
        return total

    def get_absolute_url(self):
        return reverse("order:order-summary")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20)
    products = models.ManyToManyField(CartProduct)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    order_status = models.CharField(max_length=1, choices=(
        (1, 'Pending'),
        (2, 'Confirmed'),
        (3, 'Takeaway'),
        (4, 'Delivered'),
        (5, 'Cancelled'),
        (6, 'Rejected'),
    ), default=1)
    payment_status = models.CharField(max_length=1, choices=(
        (1, 'Pending'),
        (2, 'Paid'),
        (3, 'Partial'),
        (4, 'Failed'),
    ), default=1)
    payment_method = models.CharField(max_length=1, choices=(
        (1, 'Cash'),
        (2, 'Card'),
    ), default=1)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.get_final_price()
        return total

    def get_total_quantity(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.quantity
        return total

    def get_absolute_url(self):
        return reverse("order:order-summary")


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=(
        ('B', 'Billing'),
        ('S', 'Shipping'),
    ))
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'

    def get_absolute_url(self):
        return reverse("order:order-summary")


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("order:order-summary")


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse("order:order-summary")
