"""
WSGI config for rest_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
from whitenoise.django import DjangoWhiteNoise
path='/home/moisturemonitor/moisture/django_rest/rest_api'
if path not in sys:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest_api.settings")

application = get_wsgi_application()
application=DjangoWhiteNoise(application)