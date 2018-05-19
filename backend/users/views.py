from django.shortcuts import render

# Create your views here.
from users.models import CustomUser
from users.serializers import UserSerializer
from rest_framework import generics

class UserListView(generics.ListCreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer