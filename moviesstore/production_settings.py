# Production settings for PythonAnywhere deployment
import os
from .settings import *

# Override settings for production
DEBUG = False

# Add your PythonAnywhere domain here
ALLOWED_HOSTS = ['makimsa.pythonanywhere.com', 'www.makimsa.pythonanywhere.com']

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Static files settings for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Media files settings
MEDIA_ROOT = '/home/makimsa/moviesstore/media/'
MEDIA_URL = '/media/'

# Database settings - you might want to use MySQL on PythonAnywhere
# Uncomment and configure if using MySQL:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'yourusername$moviesstore',
#         'USER': 'yourusername',
#         'PASSWORD': 'your-database-password',
#         'HOST': 'yourusername.mysql.pythonanywhere-services.com',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

# For SQLite in production (simpler but less scalable):
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/makimsa/moviesstore/db.sqlite3',
    }
}

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/makimsa/moviesstore/django_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}