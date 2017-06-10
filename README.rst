===========
justeventme
===========

Minimum-Impact Event-Sourcing Library for Django


Quick start
-----------

1. Add "justeventme" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'justeventme',
    ]


2. Run `python manage.py migrate` to create the event models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

4. Visit http://127.0.0.1:8000/admin/ to look at the event stream