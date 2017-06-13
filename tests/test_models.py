# -*- coding: utf-8 -*-

from django.test import TestCase
from justeventme.models import Event
from tests.models import TestEventType
import uuid
from django.db.utils import IntegrityError

class EventTests(TestCase):

    def test_inherited_type(self):
        b = TestEventType(test_text="blub", stream_id=uuid.uuid1(), seq=1)
        b.save()
        u = Event.objects.get(pk=b.id).get_object()
        self.assertEqual(type(u), TestEventType)

    def test_integrity_error_thrown(self):
        with self.assertRaises(IntegrityError):
            c = uuid.uuid1()
            b2 = TestEventType(test_text="blub", stream_id=c, seq=1)
            b2.save()
            b3 = TestEventType(test_text="blub", stream_id=c, seq=1)
            b3.save()

    def test_no_integrity_error_when_null(self):
        b2 = TestEventType(test_text="test1", stream_id=None, seq=None)
        b2.save()
        b3 = TestEventType(test_text="test2", stream_id=None, seq=None)
        b3.save()
        result = [x.get_object() for x in Event.objects.order_by('created')]
        self.assertEqual(result[0].payload['test_text'], 'test1')
        self.assertEqual(result[1].payload['test_text'], 'test2')

    def test_event_inheritance(self):
        t = TestEventType(test_text="blub")
        t.save()
        u = Event.objects.get(pk=t.id).get_object()
        self.assertEqual(type(u), TestEventType)

    def test_event_type_stream_id(self):
        t = TestEventType(test_text="blub", stream_id=uuid.uuid1(), seq=1)
        t.save()
        u = Event.objects.get(pk=t.id).get_object()
        self.assertEqual(type(u), TestEventType)
