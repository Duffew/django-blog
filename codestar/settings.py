"""
Django settings for codestar project.

Generated by 'django-admin startproject' using Django 4.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
# In codestar/settings.py, import the appropriate packages 
# (Note: You will use dj_database_url in a later step). 
# Now we connect the settings.py file to the env.py file:
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# create a TEMPLATES_DIR constant to build a path for our subdirectory 'templates'.
# we set TEMPLATES_DIR value to the templates directory in our base, or top-level directory.
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Modify your settings.py file to retrieve the new SECRET_KEY from the environment variables.
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['8000-duffew-djangoblog-igenqx2tywb.ws.codeinstitute-ide.net', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # add the app to the list of installed apps, surround the app name in single quotes, use a trailing comma
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_summernote',
    'blog',
    'about',
]

# We need to add a SITE_ID of 1 so that Django can handle multiple sites from one database. 
# We need to give each project an ID value so that the database is aware of which project 
# is contacting it. We only have one site here using our one database, but we'll still need to 
# tell Django the site number of 1 explicitly.
# The redirection URLs are also added so that after we've logged in or logged out, 
# the site will automatically redirect us to the home page.
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # This is the middleware for the allauth.account app you added to INSTALLED_APPS. 
    # It adds additional functionality to the project's account user authentication.
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'codestar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # add your newly created TEMPLATES_DIR constant to the list of 'DIRS'.
        # The DIRS key tells Django which directories to look in to find our templates
        'DIRS': [TEMPLATES_DIR],
        # The TEMPLATES setting also has APP_DIRS set to True, which means that Django will also look for 
        # a templates directory inside all our app directories
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

WSGI_APPLICATION = 'codestar.wsgi.application'

# Next in the settings.py file, we need to comment out the local sqlite3 database connection.
# Note: Django provides this local sqlite3 database by default for development, 
# but we are going to go with a production-ready PostgreSQL cloud database instead.

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Then, in the settings.py file, connect to the environment variable 
# DATABASE_URL you previously added to the env.py file:
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# add the following code.
# This is a list of the trusted origins for requests. As shown, you need to add both 
# your local development server URL domain 
# and your production server URL domain to allow you to add blog post content from the admin dashboard. 
# The subdomain is wildcarded with a *.
CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com"
]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# We are not using email verification in this project, so this line informs Django not to expect it. 
# Without this line, you would get Internal Server errors (code 500) during login and registration.
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# build a path for our subdirectory static so we can link to files in the static directory from a template. 
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
# This setting defines where Django will serve static files from.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
