from django.urls import path
from .views import CategoryMenuItemAPIView, MainMenuItemsAPIView, CategoryProductsAPIView

urlpatterns = [
    path('main-menu-items/', MainMenuItemsAPIView.as_view(), name='main-menu-items'),
    path('categories/<slug>/', CategoryMenuItemAPIView.as_view(), name='category-details'),
    path('categories/<slug>/products/', CategoryProductsAPIView.as_view(), name='category-products'),
]
