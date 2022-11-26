from rest_framework.serializers import ModelSerializer
from product.models import Product, Category, SubCategory, ProductImage

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        
class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
        
class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        
