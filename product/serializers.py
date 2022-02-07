from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    
    total_products = serializers.SerializerMethodField(read_only=True)
    
    def get_total_products(self, category):
        return category.products.count()
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "total_products")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        