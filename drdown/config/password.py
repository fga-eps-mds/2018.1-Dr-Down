"""
Password validation
https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
"""

# They are validators of passwords to create strong password in the system
password_validation = 'django.contrib.auth.password_validation'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': '{password}.UserAttributeSimilarityValidator'
                .format(password=password_validation),
    },
    {
        'NAME': '{password}.MinimumLengthValidator'
                .format(password=password_validation),
    },
    {
        'NAME': '{password}.CommonPasswordValidator'
                .format(password=password_validation),
    },
    {
        'NAME': '{password}.NumericPasswordValidator'
                .format(password=password_validation),
    },
]
