from __future__ import absolute_import
from celery import Celery

import os

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
app = Celery('settings', broker=settings.BROKER)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS, related_name="tasks")
app.conf.update(
        CELERY_TASK_RESULT_EXPIRES=3600
        )

if __name__ == '__main__':
    app.start()
