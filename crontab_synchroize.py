# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

    定时执行更新任务
"""
import os
import time
import schedule

from app import create_app
from utils.yaml_parse import get_yaml_data

from modules.weather.services import get_weather_info, get_precipitation
from modules.weather.models import WeatherInfoMOdel


def main():
    """"""
    root_path = os.getcwd()
    conf_city = get_yaml_data(os.path.join(root_path, 'city.yaml'))
    weather = get_weather_info(conf_city.get('stationid', 57036))
    precipitation = get_precipitation(conf_city.get('province', 'ASN'), conf_city.get('city', 'xian'))
    data = {
        'province': conf_city.get('province', 'ASN'),
        'city': conf_city.get('city', 'xian'),
        'stationid': conf_city.get('stationid', 57036),
        'weather': weather,
        'precipitation': {'hour': precipitation[0],
                          'value': precipitation[-1]},
    }
    app = create_app()
    with app.app_context():
        WeatherInfoMOdel.add_term(**data)


if __name__ == '__main__':
    # 执行命令： nohup python crontab_synchroize.py &
    # 查看进程： ps aux | grep crontab_synchroize
    # 杀死进程： kill -9 pid号
    schedule.every(60 * 60).seconds.do(main)  # TODO 设置时间， 按照秒进行设施  60* 60 即 一小时执行一次
    while True:
        schedule.run_pending()
        time.sleep(1)
