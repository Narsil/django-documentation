from django.conf import settings
import os

DOCUMENTATION_ROOT = getattr(settings, 'DOCUMENTATION_ROOT', None)
DOCUMENTATION_ACCESS_FUNCTION = getattr(settings,
    'DOCUMENTATION_ACCESS_FUNCTION', None)

if not DOCUMENTATION_ROOT:
    raise Exception('Please configure DOCUMENTATION_ROOT')
if not DOCUMENTATION_ACCESS_FUNCTION:
    raise Exception('Please configure DOCUMENTATION_ACCESS_FUNCTION')

DOCUMENTATION_HTML_ROOT = getattr(
        settings,
        'DOCUMENTATION_HTML_ROOT',
        os.path.join(DOCUMENTATION_ROOT, '_build/html/'))
DOCUMENTATION_XSENDFILE = getattr(
        settings,
        'DOCUMENTATION_XSENDFILE',
        not settings.DEBUG)
