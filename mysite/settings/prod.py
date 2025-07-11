# mysite/settings/prod.py
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com']
# final newsletter ka liya

#CORS_ALLOWED_ORIGINS = [
  #  "https://yourfrontend.com",  # ✅ sirf tumhara trusted frontend
#]

# Production-specific settings like security headers, etc. can be added here


# PostgreSQL for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mysoftwarehouse',  
        'USER': 'postgres',            # or your PostgreSQL username
        'PASSWORD': '***REMOVED***',   # replace with your actual password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Optional: add production CORS or security headers here later
