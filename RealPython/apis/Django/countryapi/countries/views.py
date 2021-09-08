"""
This replaces your client
Viewsets gets you the equivalent HTTP calls
"""

from django.shortcuts import render
from rest_framework import viewsets
from .models import Country
from .serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
