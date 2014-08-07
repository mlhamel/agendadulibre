from werkzeug import run_simple, DebuggedApplication
from django.core.handlers.wsgi import WSGIHandler

import os


def debug(host='0.0.0.0', port=8976):
    """ """
    # This is only needed for Django versions < [7537]:
    def null_technical_500_response(request, exc_type, exc_value, tb):
        raise exc_type, exc_value, tb
    from django.views import debug
    debug.technical_500_response = null_technical_500_response

    os.environ['DJANGO_SETTINGS_MODULE'] = 'agenda.production'

    run_simple(host, port, DebuggedApplication(WSGIHandler(), True))
