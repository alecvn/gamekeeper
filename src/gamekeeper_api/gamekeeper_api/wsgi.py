"""
WSGI config for gamekeeper_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys


os.environ["DJANGO_SETTINGS_MODULE"] = "gamekeeper_api.settings"

PROJECT_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..")
os.environ["HOME"] = PROJECT_ROOT

sys.stdout = sys.stderr
sys.path.insert(0, os.path.join(PROJECT_ROOT, "gamekeeper_api"))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "gamekeeper_api", "gamekeeper_api"))
sys.path.insert(2, os.path.join(PROJECT_ROOT, "venv","lib","python2.7","site-packages"))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
