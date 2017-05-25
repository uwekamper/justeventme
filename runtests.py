#!/usr/bin/env python

import os, sys
from envparse import env
from django.conf import settings
import django

DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=(
        'django.contrib.postgres',
        'model_utils',
        'justeventme',
        'tests',
    ),
    DATABASES={
        "default": {
        #    "ENGINE": "django.db.backends.sqlite3"
        #}
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'justeventme',
        'HOST': '',
        'PORT': '5432',
        'USER': env.str('DBUSER'),
        'PASSWORD': env.str('DBPASSWD'),
        }
    },
    #SILENCED_SYSTEM_CHECKS=["1_7.W001"],
)


def runtests():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    from django.test.runner import DiscoverRunner
    runner_class = DiscoverRunner
    test_args = ['tests']

    failures = runner_class(
        verbosity=1, interactive=True, failfast=False).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()