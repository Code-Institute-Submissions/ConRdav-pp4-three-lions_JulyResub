"""
WSGI config for threelions project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threelions.settings')

application = get_wsgi_application()
application = WhiteNoise(application,  root="/static/")
# application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
