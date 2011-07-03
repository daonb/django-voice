============
Django Voice
============

DjangoVoice is a very simple application to enable user feedback that is integrated with your Django project.

Originally built for Verb (http://verbapp.com), and can be seen working at Verb feedback (that is a live site, please do not use it to try out the system).

Installation and Dependencies
=============================

Firtsly you have to satisfy dependencies which described in REQUIREMENTS file. Easy way to do is using `pip installer <http://www.pip-installer.org/en/latest/index.html>`_ with -r parameter.

::

  pip -r REQUIREMENTS


this command will download and install dependencies required for django voice. After satisfying dependencies second step is activating helper applications to run.

 * Activate django's comment system. (Described 'here <https://docs.djangoproject.com/en/dev/ref/contrib/comments/>'_.)
 * Add django-gravatar and django-voting to your INSTALLED_APPS in settings file.

After you do these, your INSTALLED_APPS must be like this:

::
  
  INSTALLED_APPS = (
      ...
      ...
      ...
      'voting',
      'gravatar',
      'djangovoice'
  )

and urls.py like this:

::

  
