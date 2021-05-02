from django.urls import path

from Front_end.views import index, dashboard, charts, tables

urlpatterns = [
    path('',index, name='index'),
    path('dashboard/',dashboard, name='dashboard'),
    path('charts/',charts, name='charts'),   
    path('tables/',tables, name='tables'),



]    