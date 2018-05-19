# api/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('lead/', views.ListLead.as_view()),
    path('lead/<int:pk>/', views.DetailLead.as_view()),
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]