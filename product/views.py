from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from product.serializers import ProductSerializer, CategorySerializer, SubCategorySerializer, ProductImageSerializer
from product.models import Product, Category, SubCategory, ProductImage
# Create your views here.
