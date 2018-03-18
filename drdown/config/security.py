"""
Quick-start development settings - unsuitable for production
See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
"""
import os

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'ha*el@35h++0yux@e0henkh9^#=0z!1z@f!x(j+2@5!v2k2=f$'
)
