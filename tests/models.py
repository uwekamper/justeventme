# -*- coding: utf-8 -*-
from justeventme.models import Event


class TestEventType(Event):
    """
    A test class
    Must be in this module because of django model Reasons.
    """
    def __init__(self, bla, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payload = dict(bla=bla)

    class Meta:
        proxy = True

