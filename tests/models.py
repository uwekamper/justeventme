# -*- coding: utf-8 -*-
from justeventme.models import BaseEvent


class TestEventType(BaseEvent):
    """
    A test class
    Must be in this module because of django model Reasons.
    """
    class Meta:
        proxy = True
