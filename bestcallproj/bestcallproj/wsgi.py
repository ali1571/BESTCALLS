"""
WSGI config for bestcallproj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Update this line to match your double-nested folder structure
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bestcallproj.bestcallproj.settings')

application = get_wsgi_application()
app = application