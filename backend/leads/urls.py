from django.urls import include, path

from . import views

urlpatterns = [
  path('', views.ListLead.as_view()),
  path('<int:pk>/', views.DetailLead.as_view()),
]