from .base import *

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
