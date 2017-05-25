# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.postgres.fields import HStoreField
from model_utils.managers import InheritanceManager
from django.db.models.base import ModelBase


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


class BaseEvent(models.Model):
    """
    Events are simplistic way of keeping a log of all the changes
    in our database.
    """
    __metaclass__ = BaseEventMetaclass
    type = models.CharField(max_length=255)
    object_class = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.object_class:
            self.object_class = self._meta.object_name
        super(BaseEvent, self).save(*args, **kwargs)

    def get_object(self):
        SUBCLASSES_OF_ANIMAL = dict([(cls.__name__, cls) for cls in BaseEvent.__subclasses__()])
        if self.object_class in SUBCLASSES_OF_ANIMAL:
            self.__class__ = SUBCLASSES_OF_ANIMAL[self.object_class]
        return self

    created = models.DateTimeField(auto_now_add=True)
    # guid =
    # sequence =
    data = HStoreField()

    #class Meta:
    #    abstract = True
    objects = InheritanceManager()

    @property
    def event_type(self):
        """
        Returns the class name.
        """
        return self.get_object().__class__.__name__

    # queryset_class = HStoreQuerySet
    # event_type = models.IntegerField()

    def __str__(self):
        return '{} - {}: {}'.format(self.__class__.__name__, self.created, self.data)
