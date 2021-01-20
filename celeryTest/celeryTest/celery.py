from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery import shared_task
from celery.schedules import crontab
from celery import app as celery_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryTest.settings')

app = Celery('celeryTest',include=['celeryTest.tasks'])


app.conf.beat_schedule = {
    'every-1-minute': {
        'task': 'celeryTest.tasks.say_hello',
        'schedule': crontab(),
#        'args': (,)
    }
}

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

@app.task
def test(arg):
    print(arg)
    from celeryTest.tasks import test
    test(arg)

# get_task = PeriodicTask.objects.get(id=1)
# get_task_registed_taskname = get_task.task
# get_task_kwargs = json.loads(get_task.kwargs)

# send_task(get_task_registed_taskname,[],get_task_kwargs)

# Load task modules from all registered Django app configs.

app.autodiscover_tasks()
