# Compare to: Ecommerce/order/serializers.py

from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework import views
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .serializers import CartSerializer, CartProductSerializer, OrderSerializer, AddressSerializer, PaymentSerializer, CouponSerializer
from .models import Cart, CartProduct, Order, Address, Payment, Coupon
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.response import Response
# Create your views here.
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
class CartProductView(generics.ListCreateAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return CartProduct.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class CartProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return CartProduct.objects.filter(user=self.request.user)
    
    
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class AddressView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    
class PaymentView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)
    
class CouponView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Coupon.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class CouponDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Coupon.objects.filter(user=self.request.user)
    
class AddToCartView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
        if created:
            cart_product.quantity = quantity
            cart_product.save()
        else:
            cart_product.quantity += quantity
            cart_product.save()
        return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)
    
class RemoveFromCartView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
        if created:
            return Response({'message': 'Product not in cart'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            cart_product.delete()
            return Response({'message': 'Product removed from cart'}, status=status.HTTP_200_OK)




