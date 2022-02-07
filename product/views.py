
from rest_framework import filters, viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from .models import Product , Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter , DjangoFilterBackend)
    filterset_fields = ['category', 'price', 'created_at', 'updated_at']
    ordering_fields = ['price', 'created_at', 'updated_at']


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsListByCategory(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field_kwarg = 'category_id'

    def get_queryset(self, **kwargs):
        products = Product.objects.filter(category_id=self.kwargs['category_id'])
        return products

    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)