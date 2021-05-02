from django.core import validators
from django import forms
from .models import Donor
from django.forms import ModelForm,models
from django.forms import widgets
# from django import template

# register = template.Library()


class DonorRegistragion(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['donor_name', 'donor_email', 'donor_DOB', 'donor_gender', 'donor_phone', 'donor_address', 'donor_blood_group']
        # widgets = {
        #     'donor_name': forms.TextInput(attrs={'class':'form-control'}),
        #     'donor_email': forms.EmailField(attrs={'class':'form-control'}),
        #     'donor_DOB': forms.DateField(attrs={'class':'form-control'}),
        #     'donor_gender': forms.TextInput(attrs={'class':'form-control'}),
        #     'donor_phone': forms.TextInput(attrs={'class':'form-control'}),
        #     'donor_address': forms.TextInput(attrs={'class':'form-control'}),
        #     'donor_blood_group': forms.TextInput(attrs={'class':'form-control'}),
        # }