# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
import logging.config
from settings import DEBUG_LOG_PATH, ERROR_LOG_PATH, CELERY_LOG_PATH

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'format': '%(asctime)s \"%(filename)s:%(funcName)s:%(lineno)d\" [%(levelname)s]- %(message)s'
        }
    },
    'handlers': {
        'console': {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        'celery_handler': {
            # 'level': 'INFO',
            # 'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': CELERY_LOG_PATH,
            'when': 'midnight',
            'encoding': 'utf-8',
        },
        'weather_handler': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': DEBUG_LOG_PATH,
            'when': 'midnight',
            'encoding': 'utf-8',
        },
        'weather_err_handler': {
            'level': 'ERROR',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': ERROR_LOG_PATH,
            'when': 'midnight',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'celery_logger': {
            'handlers': ['celery_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'myapp_logger': {
            'handlers': ['weather_handler', 'weather_err_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

logging.config.dictConfig(LOG_CONFIG)
app_logger = logging.getLogger("myapp_logger")
celery_logger = logging.getLogger("celery_logger")

