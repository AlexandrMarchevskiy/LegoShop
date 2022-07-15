from rest_framework import generics, viewsets
from .serializers import ShopSerializer, CategorySerializer
from shop.models import Product, Category

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-price')
    serializer_class = ShopSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
