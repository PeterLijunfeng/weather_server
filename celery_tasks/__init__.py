# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:


    celery -A celery_tasks worker -B -l info -c 3
    nohup celery -A celery_tasks worker -B -l info -c 3 &
"""
from __future__ import absolute_import
from celery import Celery

app = Celery("weather_server")

# 导入celery的配置信息
app.config_from_object("config.py")
