from __future__ import absolute_import

from celeryTest.celery import app


# @app.task
# def add(x, y):
#     return x + y


# @app.task
# def mul(x, y):
#     return x * y


# @app.task
# def xsum(numbers):
#     return sum(numbers)

@app.task
def say_hello():
    print('hi')
    return 'hi'