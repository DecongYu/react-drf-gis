from .base import *


# https://docs.djangoproject.com/en/4.0/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_USE_TSL = True
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'info@DecongYu.com'
DOMAIN = env('DOMAIN')
SITE_NAME = 'DecongYu.com'

# To create a postgres or postgis database for Django backends
# https://hatarilabs.com/ih-en/how-to-install-postgresql-and-postgis-in-windows-10-with-wsl-and-debian-tutorial
# https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-database
DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE'),
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}
