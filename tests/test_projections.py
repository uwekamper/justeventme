# -*- coding: utf-8 -*-
from django.test import TestCase

from justeventme.projections import Projection
from justeventme.projections import register_projections
from justeventme.projections import projector_pool
from justeventme.projections import handle_event

from tests.models import TestEventType
from tests.models import TestAggregate


class MyTestProjection(Projection):
    """
    A projection that we will use later to test the projection machinery.
    """
    def __init__(self):
        super().__init__()
        self.register(TestEventType, self.handle_test_event)

    def handle_test_event(self, event):
        agg = TestAggregate(test_text=event.payload['test_text'])
        agg._super_save()


class ProjectionTests(TestCase):
    def setUp(self):
        # Register the projection class
        register_projections([
            MyTestProjection,
        ])

    def test_register(self):
        """
        Test if registering a projector class worked.
        """
        self.assertEqual(projector_pool[0], MyTestProjection)

    def test_projection_works(self):
        TEST_TEXT = "projections_test"
        t = TestEventType.objects.create(test_text=TEST_TEXT)

        # do the projection
        handle_event(t)

        # After the projection has finished there should be one aggregate with
        # the text set.
        agg = TestAggregate.objects.last()
        print(agg)
        self.assertEqual(agg.test_text, TEST_TEXT)

