# api/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('lead/', views.ListLead.as_view()),
    path('lead/<int:pk>/', views.DetailLead.as_view()),
]