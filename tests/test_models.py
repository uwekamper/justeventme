# -*- coding: utf-8 -*-

from django.test import TestCase
from justeventme.models import BaseEvent
from .models import TestEventType

class BaseEventTests(TestCase):

    def test_event_type(self):
        t = TestEventType(data=dict(bla="blub"))
        t.save()
        u = BaseEvent.objects.get(pk=t.id).get_object()
        self.assertEqual(type(u), TestEventType)