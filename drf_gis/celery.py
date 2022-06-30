from __future__ import absolute_import

import os

from celery import Celery
from drf_gis.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_gis.settings.development")

app = Celery("drf_gis")

app.config_from_object("drf_gis.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
