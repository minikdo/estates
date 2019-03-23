from .base import * # noqa F403

DEBUG = False

ALLOWED_HOSTS += [  # noqa F405
    '172.104.129.103',
    'test.domino.nieruchomosci.pl',
    'domino.nieruchomosci.pl',
    'www.domino.nieruchomosci.pl',
]

LATEX_GRAPHICSPATH = '/home/domino/sites/pix2/'
