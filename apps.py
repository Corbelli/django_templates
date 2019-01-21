import logging
from django.apps import AppConfig


class ExpeerhitsConfig(AppConfig):
    name = 'expeerhits'

    def ready(self):
        from .hits import handler
        from djangoanalytics import views
        views.handler = handler
