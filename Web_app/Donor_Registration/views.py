from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import DonorRegistragion
from Donor_Registration.models import Donor
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

# from Donor_Registration.models import Donor import csv

import csv  
# Create your views here.

# add the donor
def add_donor(request):
    if request.method == 'POST':
        fm = DonorRegistragion(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['donor_name']
            email = fm.cleaned_data['donor_email']
            dob = fm.cleaned_data['donor_DOB']
            gender = fm.cleaned_data['donor_gender']
            phone = fm.cleaned_data['donor_phone']
            address = fm.cleaned_data['donor_address']
            b_group = fm.cleaned_data['donor_blood_group']
            reg = Donor(donor_name =name, donor_email=email, donor_DOB=dob, donor_gender=gender, donor_phone=phone, donor_address=address, donor_blood_group=b_group)
            reg.save()
            messages.info(request,'Successfully, Donor are add in Donor list!!')
            fm = DonorRegistragion()
    else:
        fm = DonorRegistragion()
    return render(request, 'enroll/adddonor.html', {'form':fm})




# show the donor list
def show_donor(request):
    show_donor = Donor.objects.all()
    return render(request, 'tables.html',{'donor_list':show_donor})


# this function edit or update the donor information
def update_donor(request, id):
    if request.method == 'POST':
        donor_obj = Donor.objects.get(pk=id)
        form = DonorRegistragion(request.POST, instance=donor_obj)
        if form.is_valid():
            form.save()
    else:
        donor_obj = Donor.objects.get(pk=id)
        form = DonorRegistragion(instance=donor_obj)
    return render(request, 'enroll/updateDonor.html', {'form':form})



# this function will delete the donor from donor list
def delete_donor(request, id):
    if request.method == 'POST':
     donor_obj = Donor.objects.get(pk=id)
     donor_obj.delete()
     return redirect('/show_Donor')

#this function search the donor
def search_donor(request):
    if 'search_donor' in request.GET:
        search_donor=request.GET.get('search_donor','')
        search=Donor.objects.filter(Q(donor_address__icontains=search_donor)| Q(donor_blood_group__icontains=search_donor))
    else:
        search=Donor.objects.all()

    #pagination
    paginator=Paginator(search,2)
    page_number=request.GET.get('page')
    search_obj=paginator.get_page(page_number)
    return render(request,'enroll/searchDonor.html',{'search':search_obj})    



  
def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    donors = Donor.objects.all()  
    writer = csv.writer(response)  
    for donor in donors:  
        writer.writerow([donor.donor_name,donor.donor_email,donor.donor_DOB,donor.donor_gender,donor.donor_phone,donor.donor_address,donor.donor_blood_group])  
    return response   