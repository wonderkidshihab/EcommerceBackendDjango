from django.urls import path
from .views import CartView, CartDetailView, CartProductView, CartProductDetailView, OrderView, OrderDetailView, AddressView, AddressDetailView, PaymentView, PaymentDetailView, CouponView, CouponDetailView, AddToCartView, RemoveFromCartView
urlpatterns = [
    path('', CartView.as_view()),
    path('<int:pk>/', CartDetailView.as_view()),
    path('products/', CartProductView.as_view()),
    path('products/<int:pk>/', CartProductDetailView.as_view()),
    path('orders/', OrderView.as_view()),
    path('orders/<int:pk>/', OrderDetailView.as_view()),
    path('addresses/', AddressView.as_view()),
    path('addresses/<int:pk>/', AddressDetailView.as_view()),
    path('payments/', PaymentView.as_view()),
    path('payments/<int:pk>/', PaymentDetailView.as_view()),
    path('coupons/', CouponView.as_view()),
    path('coupons/<int:pk>/', CouponDetailView.as_view()),
    path('add-to-cart/', AddToCartView.as_view()),
    path('remove-from-cart/', RemoveFromCartView.as_view()),
]
