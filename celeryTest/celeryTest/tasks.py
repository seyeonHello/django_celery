from __future__ import absolute_import

from celeryTest.celery import app
from celery import shared_task
@shared_task
def say_hello():
    print('hi')

@shared_task
def test(arg):
    print('world')