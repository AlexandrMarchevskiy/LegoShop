from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views



router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'categories', views.CategoryViewSet, basename='categories')


urlpatterns = [
    path('api/', include(router.urls)),
]