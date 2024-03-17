import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OJSB.settings')

app = Celery('OJSB')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'addData_every_two_minutes': {
        'task': 'finance_exchange_rates.tasks.refreshData',
        'schedule': crontab(minute='*/2'),
    },
}