from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from leads import models
from . import serializers

class ListLead(generics.ListCreateAPIView):
    queryset = models.Lead.objects.all()
    serializer_class = serializers.LeadSerializer


class DetailLead(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Lead.objects.all()
    serializer_class = serializers.LeadSerializer