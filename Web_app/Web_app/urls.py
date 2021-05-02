"""Web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include ,path
from Donor_Registration import views
from Notification import views
from Front_end import views
from Contact import views

urlpatterns = [
    path('', include('polls.urls')),
    path('', include('Front_end.urls')),
    path('admin/', admin.site.urls),
    path('',include('Login.urls')),
    path('',include('Donor_Registration.urls')),
    path('',include('Notification.urls')),
    path('',include('Contact.urls')),
]

