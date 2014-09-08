from agenda.settings import *

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.mysql',
        "NAME": 'agenda',
        "USER": 'agenda',
        "PASSWORD": 'Eegh0Im7',
        "HOST": '127.0.0.1',
        "PORT": '3306',
        }
    }

DEBUG = False
ENABLE_MAIL = True
TEMPLATE_DEBUG = DEBUG
