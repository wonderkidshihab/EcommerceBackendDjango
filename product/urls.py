from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail, SubCategoryList, SubCategoryDetail, ProductImageList, ProductImageDetail
urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('subcategories/', SubCategoryList.as_view()),
    path('subcategories/<int:pk>/', SubCategoryDetail.as_view()),
    path('productimages/', ProductImageList.as_view()),
    path('productimages/<int:pk>/', ProductImageDetail.as_view()),
]