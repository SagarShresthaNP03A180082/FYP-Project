from django.shortcuts import render,redirect
from Contact.models import Contact
from django.http import HttpResponse
from django.contrib import messages
from Contact.models import Contact

# Create your views here.

def Contactus(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        messages.success(request, 'Message submission successful')
    return render(request,'index.html')

# show the Contact list
def show_contact(request):
    contact_list = Contact.objects.all()
    return render(request, 'dashboard_base.html',{'contact_list':contact_list})

def delete_message(request, id):
    if request.method == 'POST':
     contact_obj = Contact.objects.get(pk=id)
     contact_obj.delete()
     return redirect('/show_contact')
