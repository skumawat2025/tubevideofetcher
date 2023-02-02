import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tubefetch.settings')

#Initialize a new Celery application with the name 'tubefetch'.
app = Celery('tubefetch')

# This line configures the Celery application app by reading
# configuration options from the Django settings module `django.conf:settings`
# and applying all celery-related configuration keys with a CELERY_ prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# This line automatically loads task modules from all registered Django apps.
app.autodiscover_tasks()

# This line defines a Celery task named 'debug_task' and makes the
# self parameter available inside the task function, so that task-related
# information can be accessed, for example, `self.request`.
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# This line schedules the update_videos_task task to run every minute.
app.conf.beat_schedule = {
    'update_videos_task': {
        'task' : 'videofetcher.task.update_videos_task',
        'schedule' : crontab(minute='*/1'),
    },
}