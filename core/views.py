from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import viewsets
from .models import Company, Product
from .serializers import CompanySerializer, ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyView(ListView):
    template_name="templates/company.html"
    model = Company
    context_object_name = "company"