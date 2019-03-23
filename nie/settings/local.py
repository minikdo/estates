from .base import * # noqa 

DEBUG = True

INSTALLED_APPS += ['debug_toolbar', 'django_extensions']  # noqa
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa

INTERNAL_IPS = ['127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LATEX_GRAPHICSPATH = '/home/domino/pics/pix2/'
