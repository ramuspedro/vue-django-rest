# api/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('leads/', include('leads.urls')),
    path('users/', include('users.urls')),
    path('chats/', include('chat.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]