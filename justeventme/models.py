# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.base import ModelBase
from django.contrib.postgres.fields import HStoreField


class ReadModel(models.Model):
    """
    The read model is an abstract class for creating read-only models
    that present the state of the system to the outside.
    """
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Disable the save method
        """
        raise NotImplementedError()

    def _super_save(self, *args, **kwargs):
        super(ReadModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Disable the delete method.
        """
        raise NotImplementedError()

    def _super_delete(self, *args, **kwargs):
        super(ReadModel, self).delete(*args, **kwargs)
        

class BaseEventMetaclass(ModelBase):
    def __call__(cls, *args, **kwargs):
        obj = super(BaseEventMetaclass, cls).__call__(*args, **kwargs)
        return obj.get_object()


class Event(models.Model):
    """

    """
    __metaclass__ = BaseEventMetaclass

    object_class = models.CharField(max_length=1024)
    stream_id = models.UUIDField(null=True, blank=True)
    seq = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    payload = HStoreField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.object_class:
            self.object_class = self._meta.object_name
        super().save(*args, **kwargs)

    def get_object(self):
        """
        After retrieving the Event object from the database this methods is
        used to get the
        """
        SUBCLASSES_OF_EVENT = dict([(cls.__name__, cls) for cls in Event.__subclasses__()])
        if self.object_class in SUBCLASSES_OF_EVENT:
            self.__class__ = SUBCLASSES_OF_EVENT[self.object_class]
        return self

    class Meta:
        unique_together=('stream_id', 'seq')

