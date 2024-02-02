from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategoryDetailsSerializer, MainMenuItemSerializer, ProductDetailsSerializer


class MainMenuItemsAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        main_menu_items = Category.objects.filter(is_menu=True, is_active=True)
        serializer = MainMenuItemSerializer(main_menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryMenuItemAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get_menu_for_category(self, category):
        if category.parent:
            parent_category = Category.objects.get(id=category.parent.id, is_active=True)
            return self.get_menu_for_category(parent_category)
        else:
            serializer = CategoryDetailsSerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, slug, format=None):
        try:
            category = Category.objects.get(slug=slug, is_active=True)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        return self.get_menu_for_category(category)


class CategoryProductsAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, slug, format=None):
        try:
            category = Category.objects.get(slug=slug, is_active=True)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductDetailsSerializer(category.get_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)