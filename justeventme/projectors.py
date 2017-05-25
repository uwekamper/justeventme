# -*- coding: utf-8 -*-
from decimal import Decimal
from django.utils.timezone import now


def is_true(value):
    return value.lower() == 'true'


class HandlerNotFoundException(Exception):
    pass


projector_pool = []


def register_projector(projector_class):
    global projector_pool
    projector_pool.append(projector_class)


def handle_event(event):
    global projector_pool
    for projector_class in projector_pool:
        projector = projector_class()
        projector._handle_event(event)


class Projector(object):
    """
    Abstract projector class. Contains registry.
    """
    def __init__(self):
        self.registry = {}

    def _handle_event(self, event):
        try:
            handler_func = self.registry[type(event)]
        except KeyError as e:
            # raise HandlerNotFoundException()
            return

        handler_func(event)

    def register(self, event_type, handler_func):
        self.registry[event_type] = handler_func
