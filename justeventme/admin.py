# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import BaseEvent


class BaseEventAdmin(admin.ModelAdmin):
    list_display = ('created', 'event_type', 'data')

    def get_queryset(self, request):
        queryset = super(BaseEventAdmin, self).get_queryset(request)
        return queryset.select_subclasses()


admin.site.register(BaseEvent, BaseEventAdmin)

