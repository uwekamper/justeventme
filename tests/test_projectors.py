# -*- coding: utf-8 -*-
from django.test import TestCase

from justeventme.models import BaseEvent
from justeventme.projectors import Projector
from justeventme.projectors import register_projector
from justeventme.projectors import projector_pool
from .models import TestEventType

class ProjectorTests(TestCase):
    def setUp(self):
        class MyTestProjector(Projector):
            def __init__(self):
                self.register(TestEventType, self.handle_test_event)

            def handle_test_event(self, event):
                pass

        self.ProjectorClass = MyTestProjector

    def test_register(self):
        """
        Test if registering a projector class works.
        """
        register_projector(self.ProjectorClass)
        self.assertEqual(
            projector_pool[0],
            self.ProjectorClass
        )


    def test_projector(self):
        t = TestEventType(data=dict(bla="blub"))
        t.save()
        u = BaseEvent.objects.get(pk=t.id).get_object()
        self.assertEqual(type(u), TestEventType)