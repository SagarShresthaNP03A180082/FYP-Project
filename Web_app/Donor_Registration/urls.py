from django.urls import path 
from Donor_Registration.views import add_donor
from Donor_Registration.views import show_donor
from Donor_Registration.views import delete_donor
from Donor_Registration.views import update_donor
from Donor_Registration.views import search_donor
from Donor_Registration.views import getfile


urlpatterns = [
     path("add_donor/",add_donor, name="add_donor"),
     path("show_Donor/",show_donor, name="show_donor"),
     path("delete_donor/<int:id>",delete_donor, name="delete_donor"),
     path("update_donor/<int:id>",update_donor, name="update_donor"),
     path("search_donor/",search_donor, name="search_donor"),
     path("csv",getfile, name="csv"),

]    