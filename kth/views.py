from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Doctor, NewsItem
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
 return render(request, 'about.html')

#   @login_required(login_url='login')
def departments_list(request):
 departments = Department.objects.all()
 return render(request, 'departments.html', {'departments': departments})

#@login_required(login_url='login')
def department_detail(request, slug):
    department = get_object_or_404(Department, slug=slug)
    return render(request, 'departments_detail.html', {'department': department})
   
#@login_required(login_url='login')  
def doctors_list(request):
 doctors = Doctor.objects.select_related('specialty').all()
 return render(request, 'doctors.html', {'doctors': doctors})

#@login_required(login_url='login')
def doctor_detail(request, pk):
 doctor = get_object_or_404(Doctor, pk=pk)
 return render(request, 'doctor_detail.html', {'doctor': doctor})


def contact(request):
   sent = False
   if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
          form.save()
          sent = True
   else:
        form = ContactForm()
   return render(request, 'contact.html', {'form': form, 'sent': sent})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')  # redirect to your home page
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'kth/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

