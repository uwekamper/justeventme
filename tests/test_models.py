# -*- coding: utf-8 -*-

from django.test import TestCase
from justeventme.models import Event
from tests.models import TestEventType
import uuid
from django.db.utils import IntegrityError

class EventTests(TestCase):

    def test_inherited_type(self):
        b = TestEventType(bla="blub", stream_id=uuid.uuid1(), seq=1)
        b.save()
        u = Event.objects.get(pk=b.id).get_object()
        self.assertEqual(type(u), TestEventType)

    def test_integrity_error_thrown(self):
        with self.assertRaises(IntegrityError):
            c = uuid.uuid1()
            b2 = TestEventType(bla="blub", stream_id=c, seq=1)
            b2.save()
            b3 = TestEventType(bla="blub", stream_id=c, seq=1)
            b3.save()

    def test_no_integrity_error_when_null(self):
        b2 = TestEventType(bla="test1", stream_id=None, seq=None)
        b2.save()
        b3 = TestEventType(bla="test2", stream_id=None, seq=None)
        b3.save()
        result = [x.get_object() for x in Event.objects.order_by('created')]
        self.assertEqual(result[0].payload['bla'], 'test1')
        self.assertEqual(result[1].payload['bla'], 'test2')

    def test_event_inheritance(self):
        t = TestEventType(bla="blub")
        t.save()
        u = Event.objects.get(pk=t.id).get_object()
        self.assertEqual(type(u), TestEventType)

    def test_event_type_stream_id(self):
        t = TestEventType(bla="blub", stream_id=uuid.uuid1(), seq=1)
        t.save()
        u = Event.objects.get(pk=t.id).get_object()
        self.assertEqual(type(u), TestEventType)
