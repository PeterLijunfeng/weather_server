# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
import os

from utils.yaml_parse import get_yaml_data

from . import app as celery_app


@celery_app(task='', rote='', queue='')
def synchronize_weather_info():
    root_path = os.getcwd()
    conf_city = get_yaml_data(os.path.join(root_path, 'city.yaml'))
    # TODO
