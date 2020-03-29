# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""

from utils.db_mysql import db
from .controller import weather_site


def init_app(app):
    db.init_app(app)
