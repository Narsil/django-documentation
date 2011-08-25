# Create your views here.
from django.http import HttpResponse
from app_settings import DOCUMENTATION_HTML_ROOT, DOCUMENTATION_XSENDFILE,\
        DOCUMENTATION_ACCESS_FUNCTION
from django.contrib.auth.decorators import user_passes_test
import django
import mimetypes


@user_passes_test(DOCUMENTATION_ACCESS_FUNCTION)
def documentation(request, path):
    if not DOCUMENTATION_XSENDFILE:
        return django.views.static.serve(
                request,
                path,
                DOCUMENTATION_HTML_ROOT)
    mimetype, encoding = mimetypes.guess_type(path)
    response = HttpResponse(mimetype=mimetype)

    response['Content-Encoding'] = encoding
    response['Content-Disposition'] = ''
    response['X-Sendfile'] = "".join([DOCUMENTATION_HTML_ROOT, path])
    return response
