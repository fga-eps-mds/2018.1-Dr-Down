"""
File to enter application dependencies in development and
production environments
"""

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

LOCAL_APPS = [
    'user',
]

EXTERNAL_APPS = [
    'rolepermissions'
]

PRODUCTION_APPS = DJANGO_APPS + LOCAL_APPS + EXTERNAL_APPS

DEVELOPMENT_APPS = ['django_extensions'] + PRODUCTION_APPS
