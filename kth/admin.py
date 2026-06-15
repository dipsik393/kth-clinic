from django.contrib import admin
from .models import Department, Doctor, NewsItem, ContactMessage, Patient, Appointment
# Register your models here.
 
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(NewsItem)
admin.site.register(ContactMessage)
admin.site.register(Patient)
admin.site.register(Appointment)