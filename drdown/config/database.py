"""
File to insert the development and production database.

To more information:
https://docs.djangoproject.com/en/2.0/ref/settings/#databases
"""

import os

# Production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432'
    }
}
