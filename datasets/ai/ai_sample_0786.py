# In your project directory
django-admin startproject blog

# In the blog directory
python manage.py startapp blogapp

# In blog/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogapp.apps.BlogappConfig', # Add this line to register your app
]

# In blogapp/models.py
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title


# In blogapp/admin.py
from django.contrib import admin
from .models import Post


admin.site.register(Post)

# In blogapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name="all_posts"),
]

# In blog/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')), # Add this line
]