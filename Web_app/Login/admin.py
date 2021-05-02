from django.contrib import admin
from Donor_Registration.models import Donor
# Register your models here.
@admin.register(Donor)
class UserAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'donor_email', 'donor_DOB', 'donor_gender', 'donor_phone', 'donor_address', 'donor_blood_group')