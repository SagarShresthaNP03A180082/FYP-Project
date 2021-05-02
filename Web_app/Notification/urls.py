from django.contrib import admin
from django.urls import path ,include
from Notification.views import mail


urlpatterns = [
    path("sendNotification/",mail, name="sendMail"),
]    