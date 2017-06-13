# -*- coding: utf-8 -*-
from django.db import models
from justeventme.models import Event
from justeventme.models import ReadModel


class TestAggregate(ReadModel):
    test_text = models.CharField(max_length=20, blank=True, null=True)


class TestEventType(Event):
    """
    A test class
    Must be in this module because of django model Reasons.
    """
    def __init__(self, test_text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payload = dict(test_text=test_text)

    class Meta:
        proxy = True

