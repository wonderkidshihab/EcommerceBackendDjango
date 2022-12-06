from rest_framework import serializers
from .models import Order, Cart, CartProduct, Address, Payment, Coupon
from product.serializers import ProductSerializer
from product.models import Product

class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'quantity', 'ordered', 'created', 'updated']
        read_only_fields = ['id', 'ordered', 'created', 'updated']

class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'user', 'products', 'ordered', 'created', 'updated']
        read_only_fields = ['id', 'user', 'ordered', 'created', 'updated']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'user', 'street_address', 'apartment_address', 'country', 'zip', 'address_type', 'default']
        read_only_fields = ['id', 'user']
        
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'amount']
        read_only_fields = ['id']
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount']
        read_only_fields = ['id', 'user']
        
class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    payment = PaymentSerializer(read_only=True)
    coupon = CouponSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'ref_code', 'cart', 'address', 'payment', 'coupon', 'ordered', 'created', 'updated']
        read_only_fields = ['id', 'user', 'ref_code', 'ordered', 'created', 'updated']
