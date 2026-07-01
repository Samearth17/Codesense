# Create a project
django-admin startproject MyProject

# Create an app
python manage.py startapp MyApp

# Create the 'User' model in 'models.py'
from django.db import models

class User(models.Model):
    
    # User fields
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

# Create the 'Post' model in 'models.py'
class Post(models.Model):
    
	# Post fields
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

# Register the models in 'admin.py'
from django.contrib import admin

from .models import User, Post

admin.site.register(User)
admin.site.register(Post)