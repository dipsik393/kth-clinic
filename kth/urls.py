from django.urls import path
from . import views

app_name = 'kth'

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('departments/', views.departments_list, name='departments_list'),
path('departments/<slug:slug>/', views.department_detail, name='department_detail'),
path('doctors/', views.doctors_list, name='doctors_list'),
path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
path('contact/', views.contact, name='contact'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
]
