from .base import *


# https://mailtrap.io
EMAIL_BACKEND = 'django.core.mail.backends.smyp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'decong.yu@gmail.com'
DOMAIN = env("DOMAIN")
SITE_NAME = "drf_gis"

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
