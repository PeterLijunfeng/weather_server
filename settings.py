# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
import os

# project config
WORK_HOME = '/log'  # TODO  项目的根路径
APP_HOME_LOG = "%s/log" % WORK_HOME
API_BASE_URL = ''

if not os.path.isdir(WORK_HOME):
    os.makedirs(WORK_HOME)

if not os.path.isdir(APP_HOME_LOG):
    os.makedirs(APP_HOME_LOG)

# log
DEBUG_LOG_PATH = "%s/weather_debug.log" % APP_HOME_LOG
ERROR_LOG_PATH = "%s/weather_error.log" % APP_HOME_LOG
CELERY_LOG_PATH = "%s/celery.log" % APP_HOME_LOG

# flask
SECRET_KEY = '93544a0e0257469abf8f7dee5eaacf3bfe40cc0fa73d4142b8fad33e69f88c4f4b02dfe89080468eaf1df4881a4e905a'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16M

# weather url
WEATHER_URL = 'http://www.nmc.cn/rest/weather?stationid=%s&_=%s'
PRECIPITATION_URL = 'http://www.nmc.cn/publish/forecast/%s/%s.html'
IMG_URL = 'http://image.nmc.cn/assets/img/w/40x40/4/%s.png'

# SQL db
SQL_USER = 'root'  # TODO
SQL_PASSWD = '123456'  # TODO
SQL_HOST = '10.10.10.10'  # TODO
SQL_PORT = 3306  # TODO
SQL_DB_NAME = 'weather_server'  # TODO
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysq://%s:%s@%s:%s/%s' % \
#                           (SQL_USER, SQL_PASSWD, SQL_HOST, SQL_PORT, SQL_DB_NAME)
SQLALCHEMY_DATABASE_URI = 'sqlite:///db/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
