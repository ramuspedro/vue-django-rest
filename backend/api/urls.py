# api/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('leads/', views.ListLead.as_view()),
    path('leads/<int:pk>/', views.DetailLead.as_view()),
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]