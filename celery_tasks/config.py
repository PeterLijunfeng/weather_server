# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
from __future__ import absolute_import
from celery import platforms
from celery.schedules import crontab

# from settings import REDIS_HOST, REDIS_PORT, REDIS_PASSWD, REDIS_BROKER_DB, REDIS_RST_BAK_DB

# redis
REDIS_HOST = ''
REDIS_PORT = ''
REDIS_PASSWD = ''
REDIS_BROKER_DB = ''
REDIS_RST_BAK_DB = ''

platforms.C_FORCE_ROOT = True

BROKER_URL = 'redis://:%s@%s:%s/%s' % (REDIS_PASSWD, REDIS_HOST, REDIS_PORT, REDIS_BROKER_DB)
CELERY_RESULT_BACKEND = 'redis://:%s@%s:%s/%s' % (REDIS_PASSWD, REDIS_HOST, REDIS_PORT, REDIS_RST_BAK_DB)

CELERY_IMPORTS = (
    'timed_task',
)

CELERY_TASK_RESULT_EXPIRES = 1200
CELERYD_PREFETCH_MULTIPLIER = 4
CELERYD_MAX_TASKS_PER_CHILD = 40
CELERY_DEFAULT_QUEUE = "default"

CELERY_QUEUES = {
    "default_tasks": {  # 这是上面指定的默认队列
        "exchange": "default",
        "exchange_type": "direct",
        "routing_key": "default_dongwm"
    },
    # "topicqueue": {  # 这是一个topic队列 凡是topictest开头的routing key都会被放到这个队列
    #     "routing_key": "topictest.#",
    #     "exchange": "topic_exchange",
    #     "exchange_type": "topic",
    # },
    # "test2": {  # test和test2是2个fanout队列,注意他们的exchange相同
    #     "exchange": "broadcast_tasks",
    #     "exchange_type": "fanout",
    #     "binding_key": "broadcast_tasks",
    # },
    # "test": {
    #     "exchange": "broadcast_tasks",
    #     "exchange_type": "fanout",
    #     "binding_key": "broadcast_tasks2",
    # },
}

CELERYBEAT_SCHEDULE = {
    'timed_crontab': {
        'task': '',
        'schedule': crontab(minute=6, hour='*/1'),  # 每小时的第6分钟一次
        # 'schedule': crontab(minute=30, hour=0),  # 每天0点30分钟执行一次
        'args': ''
    }
}
