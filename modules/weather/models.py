# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
import json
from utils.db_mysql import db

from .. import CommonModel, N_DEL


class WeatherInfoMOdel(db.Model, CommonModel):
    __tablename__ = 'tbl_weather_info'

    id = db.Column(db.String(40), nullable=False, primary_key=True, index=True)
    province = db.Column(db.String(50), nullable=False, index=True, doc="省份")
    city = db.Column(db.String(50), nullable=False, index=True, doc="城市")
    stationid = db.Column(db.Integer, nullable=False, index=True, doc="站点编号")
    weather = db.Column(db.Text, default='', doc="天气")
    precipitation = db.Column(db.Text, default='', doc="降水")

    def __init__(self, *args, **kwargs):
        super(WeatherInfoMOdel, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<TAG: {self.id}>".format(self=self)

    @classmethod
    def get_one(cls, term_id, include_del=False):
        qry = cls.query
        if not include_del:
            qry = qry.filter(cls.is_del == N_DEL)
        return qry.filter(cls.id == term_id).first()

    @classmethod
    def get_one_name(cls, name, include_del=False):
        qry = cls.query
        qry = qry.filter(cls.name == name)
        if not include_del:
            qry = qry.filter(cls.is_del == N_DEL)
        return qry.first()

    @classmethod
    def get_latest_by_city(cls, city='', province=None, stationid=None, include_del=False):
        qry = cls.query
        if city:
            qry.filter(cls.city == city)
        if province:
            qry.filter(cls.province == province)
        if stationid:
            qry.filter(cls.stationid == stationid)

        if not include_del:
            qry = qry.filter(cls.is_del == N_DEL)
        qry.order_by(cls.create_at.desc())
        return qry.first()

    @classmethod
    def get_list(cls, include_del=False, page_idx=1, limit=20, **kwargs):
        qry = cls.query
        if kwargs.get('province'):
            qry = qry.filter(cls.province == kwargs.get('province'))
        if kwargs.get('city'):
            qry = qry.filter(cls.city == kwargs.get('city'))
        if kwargs.get('stationid'):
            qry = qry.filter(cls.stationid == kwargs.get('stationid'))
        if not include_del:
            qry = qry.filter(cls.is_del == N_DEL)
        return qry.count(), qry.order_by(cls.create_at.desc()).limit(limit).offset((page_idx - 1) * limit).all()

    @classmethod
    def add_term(cls, **kwargs):
        entry = cls()
        entry.id = cls().gen_uuid()

        for k, v in kwargs.items():
            if k in ['weather', 'precipitation']:
                setattr(entry, k, json.dumps(v))
            elif k in cls.__dict__.keys() and v is not None:
                setattr(entry, k, v)

        db.session.add(entry)
        db.session.commit()
        return entry
