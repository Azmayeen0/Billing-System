from rest_framework import generics
from .models import Product, Employee, Customer
from .serializers import ProductSerializer, EmployeeSerializer, CustomerSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Similar views for Employee and Customer
