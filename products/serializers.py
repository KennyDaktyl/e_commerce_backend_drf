from rest_framework import serializers
from .models import Category, Product


class MainMenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'order', 'name', 'slug']


class ProductDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class CategoryDetailsSerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'order', 'name', 'slug', 'description', 'is_active', 'parent', 'subcategories', 'get_products_count']

    def get_subcategories(self, instance):
        subcategories = Category.objects.filter(parent=instance, is_active=True).order_by('order')
        serializer = self.__class__(subcategories, many=True)
        return serializer.data if serializer.data else None