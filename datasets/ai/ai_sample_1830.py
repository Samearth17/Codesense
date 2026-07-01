# Setup Virtual Environment and Django
mkdir my_ecommerce_site
cd my_ecommerce_site
python3 -m venv venv
source venv/bin/activate
pip install django

# Create the Project
django-admin startproject ecommerce

# Create the User app and database
cd ecommerce
python manage.py startapp users
python manage.py migrate

# Add 'users' to INSTALLED_APPS in settings.py
INSTALLED_APPS = [
 'users.apps.UsersConfig',
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages'
]

# Create and register the user model
# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
 username = models.CharField(max_length=20, unique=True)
 phone_number = models.CharField(max_length=20,blank=True)
    
class Meta:
 db_table = 'users'

# admin.py
from django.contrib import admin
from .models import CustomUser
admin.site.register(CustomUser)

# Update the default User model
# settings.py

AUTH_USER_MODEL = 'users.CustomUser'

# Add users app URLs
# urls.py

from django.urls import path, include
urlpatterns = [
 path('users/', include('users.urls')),
]

# Create users app URLs
# urls.py

from django.urls import path
from .views import register, login, logout

urlpatterns = [
 path('register/', register, name="register"),
 path('login/', login, name="login"),
 path('logout/', logout, name="logout"),
]

# Create views 
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def register(request):
 if request.method == 'POST':
  form = UserCreationForm(request.POST)
  if form.is_valid():
   form.save()
   email = form.cleaned_data.get('email')
   raw_password = form.cleaned_data.get('password1')
   user = authenticate(email=email, password=raw_password)
   login(request, user)
   return redirect('home') 
 else:
  form = UserCreationForm()
 return render(request, 'register.html', {'form': form})

def login(request):
 if request.method == 'POST':
  email = request.POST.get('email')
  raw_password = request.POST.get('password')
  user = authenticate(email=email, password=raw_password)
  if user is not None:
   login(request, user)
   return redirect('home')
 else:
  return render(request, 'login.html')

def logout(request):
 logout(request)
 return redirect('login')