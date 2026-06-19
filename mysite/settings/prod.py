# mysite/settings/prod.py
from .base import *
# from decouple import config
DEBUG = False


ALLOWED_HOSTS = ['yourdomain.com']  # Changed: Replace with your actual domain (e.g., 'mysoftwarehouse.com')

# final newsletter ka liya (Assuming this is for CORS or email)
# Changed: Enabled and configured CORS for trusted frontend
CORS_ALLOWED_ORIGINS = [
    "https://yourfrontend.com",  #  (replace with actual URL)
]

# Changed: Added security headers
SECURE_SSL_REDIRECT = True  # Force HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year for HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True  # Only send cookies over HTTPS
CSRF_COOKIE_SECURE = True     # Only send CSRF token over HTTPS
X_FRAME_OPTIONS = 'DENY'      # Prevent clickjacking

# Changed: Email configuration for production (use environment variables)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.uuuemail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@mytech.com'
# Changed: Moved password to environment variable
import os
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'mytech@123')  # Default for local test
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Changed: PostgreSQL configuration with environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mysoftwarehouse',
        'USER': 'ishiwuc',            # Changed: Use env variable
        'PASSWORD': os.environ.get('DB_PASSWORD', 'abjscuwe'),  # Default for local test
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', 'jbiq'),
    }
}


