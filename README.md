# django_celery

## 스케줄러

##### ``` pip install celery>=4.4.7, <4.5 ```
##### ``` pip install django-celery-beat==2.0.0 ```

##### 프로세스 구동
##### 1. ``` celery -A celeryTest beat -l info ```
##### 매 분마다 task 구동되는지 확인
##### 2. ``` celery -A celeryTest worker -l info ```


#### 1+2. ```celery -A celeryTest worker --beat --loglevel=info```
<hr>

#### Implement dynamic adding periodic tasks
##### 1. ``` celery -A celeryTest beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler ```
##### 2. ``` celery -A celeryTest worker --loglevel=info -n worker1 ```
