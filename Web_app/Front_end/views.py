from django.shortcuts import render
from django.http import HttpResponse
from Donor_Registration.models import Donor
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



# Create your views here.

def index(request):
    return render(request,'index.html',)

def dashboard(request):
    return render(request,'dashboard_base.html',)

def charts(request):
    return render(request,'charts.html',)

def tables(request):
    return render(request,'tables.html',)


def dashboard_view(request):
    users = Users.objects.count()
    donor = Donor.objects.count()
    context = {"user_count": users, "donor": donor}
    return render(request, "dashboard.html", context)
    # User = get_user_model()
    # count = User.objects.count()
    # return render(request,'dashboard_base.html',{
    #     'count' : count
    # })
    
