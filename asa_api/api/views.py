from django.shortcuts import render
from .models import Currency
from .serializers import CurrencySerializer
from rest_framework import viewsets
# Create your views here.


class CurrencyViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
