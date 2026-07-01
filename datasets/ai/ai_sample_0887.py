# views.py
from django.shortcuts import render
import datetime

# Create your views here.
def show_time(request):
    now = datetime.datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    context = {
        'current_date_time': date_time
    }
    return render(request, 'time.html', context)

# urls.py
from django.urls import path
from .import views

urlpatterns = [
    path('time/', views.show_time, name='time'),
]

# time.html
<p>Current date and time: <strong>{{ current_date_time }}</strong></p>