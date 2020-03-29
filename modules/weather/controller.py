# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
import os
from flask import Blueprint

from settings import API_BASE_URL
from utils.rest import restful
from utils.yaml_parse import get_yaml_data

from .services import get_parse_info_comp

weather_site = Blueprint('weather', __name__, url_prefix="%s/weather" % API_BASE_URL)


@weather_site.route('/<province>/<city>/<int:stationid>', methods=["GET"])
@restful
def get_weather_city(province, city, stationid, *args, **kwargs):
    """获取城市信息

    :param province:  省份                ASN    ABJ       AGD
    :param city:      城市拼音            xian   beijing   guangzhou
    :param stationid: 编号  城市站点编号  57036   54511
    :param args:
    :param kwargs:
    :return:
    """
    return get_parse_info_comp(province, city, stationid)


@weather_site.route('/latest', methods=["GET"])
@restful
def get_weather_latest(*args, **kwargs):
    """获取配置城市最新信息

    :param args:
    :param kwargs:
    :return:
    """
    root_path = os.getcwd()
    conf_city = get_yaml_data(os.path.join(root_path, 'city.yaml'))
    province = conf_city.get('province', 'ASN')
    city = conf_city.get('city', 'xian')
    stationid = conf_city.get('stationid', 57036)
    return get_parse_info_comp(province, city, stationid)
