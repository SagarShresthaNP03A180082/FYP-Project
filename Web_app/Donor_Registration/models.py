from django.db import models

# Create your models here.
class Donor(models.Model):
    id = models.AutoField(primary_key=True)
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField(max_length=100)
    donor_DOB = models.DateField()
    donor_gender = models.CharField(max_length=10)
    donor_phone = models.CharField(max_length=10)
    donor_address = models.CharField(max_length=100)
    donor_blood_group = models.CharField(max_length=5)

