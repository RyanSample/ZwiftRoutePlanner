from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('routes/<str:route_name>/', views.detail, name='detail'),
]