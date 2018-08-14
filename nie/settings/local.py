from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'media/')  # add STATIC_ROOT to DIRS
]
