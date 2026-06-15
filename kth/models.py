from django.db import models
from django.urls import reverse




class Department(models.Model):
 name = models.CharField(max_length=120)
 summary = models.TextField(blank=True)
 slug = models.SlugField(unique=True)

 class Meta:
    verbose_name = "Department"
    verbose_name_plural = "Departments"

 def __str__(self):
    return self.name

 def get_absolute_url(self):
    return reverse('core:department_detail', kwargs={'slug': self.slug})




class Doctor(models.Model):

 first_name = models.CharField(max_length=80)
 last_name = models.CharField(max_length=80)
 title = models.CharField(max_length=80, blank=True)
 specialty = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
 bio = models.TextField(blank=True)
 photo = models.ImageField(upload_to='doctors/', blank=True, null=True)
 contact_email = models.EmailField(blank=True)

 class Meta:
    ordering = ['last_name', 'first_name'] 

 def __str__(self):
    return f"{self.title} {self.first_name} {self.last_name}".strip()




class NewsItem(models.Model):

 title = models.CharField(max_length=200)
 content = models.TextField()
 published_at = models.DateTimeField(auto_now_add=True)
 slug = models.SlugField(unique=True)

 class Meta:
    ordering = ['-published_at']

 def __str__(self):
    return self.title




class ContactMessage(models.Model):

 name = models.CharField(max_length=120)
 email = models.EmailField()
 subject = models.CharField(max_length=200, blank=True)
 message = models.TextField()
 created_at = models.DateTimeField(auto_now_add=True)

 def __str__(self):
    return f"Message from {self.name} ({self.email})"

#Scaffolding for future full system:



class Patient(models.Model):

 first_name = models.CharField(max_length=80)
 last_name = models.CharField(max_length=80)
 email = models.EmailField(unique=True)
 phone = models.CharField(max_length=30, blank=True)
 date_of_birth = models.DateField(null=True, blank=True)

 def __str__(self):
    return f"{self.first_name} {self.last_name}"




class Appointment(models.Model):
 patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
 doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
 department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
 scheduled_at = models.DateTimeField()
 reason = models.TextField(blank=True)
 created_at = models.DateTimeField(auto_now_add=True)
 confirmed = models.BooleanField(default=False)

 class Meta:
    ordering = ['-scheduled_at']

 def __str__(self):
    return f"Appt {self.scheduled_at} - {self.doctor or 'TBD'}"
