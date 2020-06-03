import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduler.settings')

from celery.schedules import crontab
from django.conf import settings

redis_host = settings.REDIS_HOST


app = Celery('scheduler',
broker='redis://' + settings.REDIS_HOST + ':6379',
backend='redis://' + settings.REDIS_HOST + ':6379',
include=['scheduler_app.tasks']
)

app.conf.update(
CELERY_TASK_SERIALIZER='json',
CELERY_RESULT_SERIALIZER='json',
CELERY_TASK_RESULT_EXPIRES=3600,
CELERY_TIMEZONE='UTC',
CELERYBEAT_SCHEDULE = {
'do_task': {
'task': 'scheduler_app.tasks.do_task',
'schedule': crontab(hour='20',minute='45'),
},
}
)

if __name__ == '__main__':
    app.start()


# 'chained': {
#         'task': 'celery_tasks.add',
#         'schedule': crontab(),
#         'options': {
#             'queue': 'default',
#             'link': signature('celery_tasks.mul',
#                         args=(),
#                         kwargs={},
#                         options={
#                             'link': signature('celery_tasks.another_task', 
#                                 args=(),
#                                 kwargs={}, 
#                                 queue='default')
#                         },
#                         queue='default')
#             },
#          'args': ()
#     }