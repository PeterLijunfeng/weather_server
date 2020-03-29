# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
import json
import time
import requests
from lxml import etree

from utils.log4 import app_logger as log
from settings import WEATHER_URL, PRECIPITATION_URL, IMG_URL

from .. import NULL_DATA
from .models import WeatherInfoMOdel


def get_msec_timestamp() -> int:
    """

    :return:
    """
    return int(time.time() * 1000)


def get_weather_info(stationid: int, url=WEATHER_URL, img_url=IMG_URL) -> list:
    """爬取天气信息

    :param stationid:  站点ID
    :param url:
    :param img_url:
    :return:
    [
        {
            'date': '2020-03-25', 'pt': '2020-03-25 20:00',
            'day': {
                'weather': {'info': '9999', 'img': '9999', 'temperature': '9999'},
                'wind': {'direct': '9999', 'power': '9999'}
            },
            'night': {
                'weather': {'info': '雷阵雨', 'img': 'http://image.nmc.cn/assets/img/w/40x40/4/4.png',
                            'temperature': '21'},
                'wind': {'direct': '无持续风向', 'power': '微风'}}
        },
        ...
    ]
    """
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    req_url = url % (stationid, get_msec_timestamp())
    resp = requests.get(req_url, headers=headers)
    if not resp.ok:
        log.error('爬取气温信息，相应失败：{}'.format(resp.status_code))
        return []

    detail = resp.json().get('data', {}).get('predict', {}).get('detail', [])
    if not detail:
        log.error('爬取天气信息失败，解析信息为[]')

    try:
        for det in detail:

            day_img = det.get('day', {}).get('weather', {}).get('img', NULL_DATA)
            if day_img != NULL_DATA:
                det['day']['weather']['img'] = img_url % day_img

            night_img = det.get('night', {}).get('weather', {}).get('img', NULL_DATA)
            if night_img != NULL_DATA:
                det['night']['weather']['img'] = img_url % night_img
    except Exception as err:
        log.error('>>> get_weather_info: {}'.format(str(err)))
        return []

    return detail


def xpath_html(html_text: str) -> list:
    """

    :param html_text:
    :return:
    """
    rst = []
    body = etree.HTML(html_text)
    for i in range(7):
        day = 'day%s' % i
        elements = body.xpath('//div[@id="%s"]//div' % day)
        hours, precips = [], []
        for e in elements:
            items = list(e.xpath('.//*'))
            if len(items) == 10:
                hours.append(items[0].text.strip())
                precips.append(items[3].text.strip())
        rst.append({'hour': hours, 'value': precips})
    return rst


def get_precipitation(province: str, city_name: str, url=PRECIPITATION_URL) -> list:
    """

    :param province:  陕西 ASN     广东 AGD
    :param city_name: 西安 xian    广州 guangzhou
    :param url:
    :return:
        {"day0": {"hours": ['23:00', '26日02:00', '05:00', '08:00', '11:00', '14:00', '17:00', '20:00'],
        "value": ['-', '-', '0.2mm', '4.2mm', '3mm', '1.8mm', '0.1mm', '-']}}
    """
    headers = {'Content-Type': 'text/html'}
    req_url = url % (province, city_name)
    resp = requests.get(req_url, headers=headers)
    if not resp.ok:
        log.error('爬取降水信息，相应失败：{}'.format(resp.status_code))
        return []
    return xpath_html(resp.content)


def get_parse_info_comp(province: str, city: str, stationid: int):
    """

    :param province:
    :param city:
    :param stationid:
    :return:
    """
    try:
        weather = get_weather_info(stationid)
        precipitation = get_precipitation(province, city)
        if not weather or not precipitation:
            return {}
            # rst = WeatherInfoMOdel.get_latest_by_city(city, province, stationid)
            # if not rst:
            #     return {}
            # return {
            #     'province': province,
            #     'city': city,
            #     'stationid': stationid,
            #     'weather': json.loads(rst.weather),
            #     'precipitation': json.loads(rst.precipitation)
            # }

        data = {
            'province': province,
            'city': city,
            'stationid': stationid,
            'weather': weather,
            'precipitation': precipitation
        }
        # WeatherInfoMOdel.add_term(**data)
        return data
    except Exception as err:
        log.error('>>> 获取数据失败：{}'.format(str(err)))
        return {}
