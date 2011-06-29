``django-activeusers`` aims to keep track of currently active users on
Django-powered Web sites.

It is a reworked, simplified fork of ``django-tracking`` located at
http://bitbucket.org/codekoala/django-tracking.

Features
========

* Tracks the following information about your visitors:

    * Session key
    * IP address
    * User agent
    * Whether or not they are a registered user and logged in
    * Where they came from (http-referer)
    * What page on your site they last visited
    * How many pages on your site they have visited

* Automatic clean-up of old visitor records
* The ability to have a live feed of active users on your website
* Template tags to:

    * display how many active users there are on your site
    * determine how many active users are on the same page within your site

Requirements
============

* Django 1.2+

Installation
============

Download ``django-activeuesers`` using *one* of the following methods:

pip
---

    pip install -e git+http://github.com/asavoy/django-activeusers.git#egg=django-activeusers

Configuration
=============

First of all, you must add this project to your list of ``INSTALLED_APPS`` in
``settings.py``::

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        ...
        'django-activeusers',
        ...
    )

Run ``manage.py syncdb``.  This creates a few tables in your database that are
necessary for operation.

Depending on how you wish to use this application, you have a few options:

Visitor Tracking
----------------

Add ``django-activeusers.middleware.VisitorTrackingMiddleware`` to your
``MIDDLEWARE_CLASSES`` in ``settings.py``.  It must be underneath the
``AuthenticationMiddleware``, so that ``request.user`` exists.

Automatic Visitor Clean-Up
++++++++++++++++++++++++++

If you want to have Django automatically clean past visitor information out
your database, put ``django-activeusers.middleware.VisitorCleanUpMiddleware`` 
in your ``MIDDLEWARE_CLASSES``.

Visitors on Page (template tag)
-------------------------------

Make sure that ``django.core.context_processors.request`` is somewhere in your
``TEMPLATE_CONTEXT_PROCESSORS`` tuple.  This context processor makes the
``request`` object accessible to your templates.  This application uses the
``request`` object to determine what page the user is looking at in a template
tag.



If you don't want particular areas of your site to be tracked, you may define a
list of prefixes in your ``settings.py`` using the 
``ACTIVEUSERS_IGNORE_PREFIXES``. For example, if you didn't want visits to the 
``/family/`` section of your website, set ``ACTIVEUSERS_IGNORE_PREFIXES`` to 
``['/family/']``.

By default, active users include any visitors within the last 10 minutes.  If
you would like to override that setting, just set ``ACTIVEUSERS_TIMEOUT`` to 
however many minutes you want in your ``settings.py``.

For automatic visitor clean-up, any records older than 24 hours are removed by
default.  If you would like to override that setting, set
``ACTIVEUSERS_CLEANUP_TIMEOUT`` to however many hours you want in your
``settings.py``.

Good luck!  Please contact me with any questions or concerns you have with the
project!
