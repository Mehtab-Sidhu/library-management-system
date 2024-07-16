import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
# from library.libmgmt.tasks import remind_users_to_return_book

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("library")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.LOCAL_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     from library.libmgmt.tasks import remind_users_to_return_book

#     sender.add_periodic_task(
#         crontab(hour=12, minute=45),
#         remind_users_to_return_book.s(),
#     )

app.conf.beat_schedule = {
    'send-reminders-daily': {
        'task': 'library.libmgmt.tasks.remind_users_to_return_book',
        'schedule': crontab(hour=0, minute=0),
    },
}

