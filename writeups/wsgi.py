"""
WSGI config for writeups project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Ensure the DJANGO_SETTINGS_MODULE environment variable is set correctly
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "writeups.settings")

application = get_wsgi_application()
