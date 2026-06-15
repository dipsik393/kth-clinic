from django import forms
from .models import ContactMessage, Appointment

class ContactForm(forms.ModelForm):
 class Meta:
  model = ContactMessage
  fields = ['name', 'email', 'subject', 'message']
  widgets = {
   'message': forms.Textarea(attrs={'rows':4}),
  }

class AppointmentForm(forms.ModelForm):
 class Meta:
  model = Appointment
  fields = ['patient', 'doctor', 'department', 'scheduled_at', 'reason']
  widgets = {
   'scheduled_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
   'reason': forms.Textarea(attrs={'rows':3}),
  }
