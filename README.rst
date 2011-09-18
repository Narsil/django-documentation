=====================================
Django-documentation
=====================================

This `Django <http://djangoproject.com>`_ app has for purpose to integrate
protected sphinx based documentation .


Installation 
============

Depedencies  
~~~~~~~~~~~

django-documentation depends on `Sphinx <http://sphinx.pocoo.org>`_

Installing django-simple-feedback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install into your python path using pip::

    pip install django-documentation
    pip install -e git+git://github.com/Narsil/django-documentation.git#egg=django-documentation

Add *'documentation'* to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'documentation',
    )

Add *'(r'^docs/', include('documentation.urls')'* to your urls:: 

    urlpatterns = patterns( '',
        ....
        (r'^docs/', include('documentation.urls'),
    )

Settings
~~~~~~~~

Set up where is your documentation, and a function that has a user for argument
and returns **True** if user is allowed to see the doc. If you plan on using 
``lambda user: True``, then you probably should not be using this app, as
staticfiles would be better suited for this task. ::

    DOCUMENTATION_ROOT = '/path/to/docs/'
    DOCUMENTATION_ACCESS_FUNCTION = lambda user: user.is_staff

The DOCUMENATION_ROOT is the root of your sphinx doc where the Makefile exists, if you html docs is 
placed somewhere else than ``DOCUMENTATION_ROOT + '_build/html/'`` then you
can override it with::

    DOCUMENTATION_HTML_ROOT = '/my/other/location/

Note that django-documentation serves the content via x-sendfile when DEBUG
is False, otherwise it uses 
`django.views.static.serve <https://docs.djangoproject.com/en/dev/howto/static-files/#django.views.static.serve>`_
To override use ::

    DOCUMENTATION_XSENDFILE = True

django-documentation also comes with a command goodies ::

    ./manage.py makedoc
        
to generate the documentation.
