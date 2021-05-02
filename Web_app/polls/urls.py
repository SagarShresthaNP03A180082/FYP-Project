from django.urls import path

from . import views

urlpatterns = [
    path('demo', views.base, name='demo'),
]