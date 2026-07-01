# Creating a virtual environment
python -m venv env
source env/bin/activate
pip install Django

# Create a Django project
django-admin startproject Blog

# Create an app
cd Blog
python manage.py startapp blog_app

# Install dependencies
# Install crispy_forms to use for styling forms
pip install django-crispy-forms

# Adding applications to the settings.py
# Add the blog_app to the installed applications
INSTALLED_APPS = [
    # django dependencies
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party dependencies
    'crispy_forms', 

    #  project applications
    'blog_app',
]

# Add template settings to the settings.py
# Include the templates directory in the settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Register models and create the URL path
# Create views to handle requests
# Add templates for posts and pages
# Configure your Django admin interface
# Configure static and media files
# Start the server to see the blog