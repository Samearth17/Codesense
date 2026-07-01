# settings.py

AUTH_USER_MODEL = 'myapp.MyUser'

# models.py

from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
 first_name = models.CharField(max_length=30)
 last_name = models.CharField(max_length=30)

# forms.py

from django import forms
from myapp.models import MyUser

class MyUserForm(forms.ModelForm):
 class Meta:
 model = MyUser
 fields = ('username','password','first_name','last_name')

# views.py

from django.shortcuts import render
from myapp.forms import MyUserForm

def register(request):
 if request.method == 'POST':

  form = MyUserForm(request.POST)

  if form.is_valid():
   form.save()
   return HttpResponseRedirect('/')

 else:
  form = MyUserForm()

 return render(request, 'register.html', {'form': form})