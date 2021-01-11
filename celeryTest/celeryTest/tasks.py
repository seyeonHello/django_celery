from __future__ import absolute_import

from celeryTest.celery import app

@app.task
def say_hello():
    print('hi')
    return 'hi'