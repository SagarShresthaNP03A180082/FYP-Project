from django.urls import path 
from Contact.views import Contactus,show_contact,delete_message


urlpatterns = [
     path("Contactus/",Contactus, name="Contactus"),
     path("show_contact/",show_contact, name="show_contact"),
     path("delete_message/<int:id>",delete_message, name="delete_message"),
     

]    