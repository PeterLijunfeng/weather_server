# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
import uuid
from datetime import datetime

from utils.db_mysql import db

DEL = ON = 1
N_DEL = OFF = 0


class CommonModel(object):
    create_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, doc='创建时间')
    is_del = db.Column(db.Integer, default=N_DEL, doc="是否已删")

    @staticmethod
    def gen_uuid():
        return uuid.uuid4().hex


NULL_DATA = '9999'
