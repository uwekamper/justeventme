# -*- coding: utf-8 -*-
from django.db import transaction
from .projectors import handle_event

"""
RULES:
  * commands must only create events
  * commands never change an aggregate model themselves
  * commands never delete events, only add to the event stream.
  * you can of course check the current state of aggregate models
    to validate the input.
"""


class CommandError(Exception):
    pass


class Command(object):
    """
    Base class for commands
    """
    def __init__(self):
        self._handle()

    def pre(self):
        """
        Overwrite this method to implement a pre-hook for a command.
        """
        pass

    def main(self):
        """
        This method will always be replaced with a function
        """
        raise NotImplementedError()

    def post(self):
        """
        Overwrite this method to implement a post-hook for a command.
        """
        pass

    def _handle(self):
        self.pre()
        with transaction.atomic():
            for event in self.main():
                event.save()
                handle_event(event)
        self.post()
