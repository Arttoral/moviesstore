#!/usr/bin/env python3.11

"""
WSGI config for moviesstore project on PythonAnywhere.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

For more information visit:
https://help.pythonanywhere.com/pages/DjangoStaticFiles
"""

import os
import sys

# Add your project directory to sys.path
# This assumes your project is in /home/makimsa/moviesstore/
path = '/home/makimsa/moviesstore'
if path not in sys.path:
    sys.path.insert(0, path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesstore.production_settings')

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())