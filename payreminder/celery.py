import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "payreminder.settings")
app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'add-every-minute': {
        'task': 'task_send_notification',
        'schedule': crontab()
    },
}
app.conf.timezone = 'UTC'

