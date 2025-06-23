from .base import *

# Development-specific settings
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Email backend for testing (prints email to console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
