# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
import traceback
from functools import wraps

from flask import jsonify
from werkzeug.exceptions import HTTPException, BadRequest, InternalServerError

from .errors import ApiException, AuthException
from .log4 import app_logger as log

API_NEED_LOGIN = "L"
API_OPEN = "O"
API_CLOSE = "C"
SUPPORT_CONTROL = [API_NEED_LOGIN, API_OPEN, API_CLOSE]

WEATHER = {
    'get_weather_city': API_OPEN,
    'get_weather_latest': API_OPEN,
}

API_CONTROL = dict()
API_CONTROL.update(WEATHER)


def restful(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        headers = dict()
        headers['Content-Type'] = 'application/json'
        try:
            if func.__name__ not in API_CONTROL \
                    or API_CONTROL[func.__name__] not in SUPPORT_CONTROL \
                    or API_CONTROL[func.__name__] == API_CLOSE:
                raise ApiException(error_code=1003, msg="API NOT FOUND OR NOT SUPPORT")
            data = func(*args, **kwargs)
            rst_data = {
                "rst": "ok",
                "data": data,
            }
            return jsonify(rst_data), 200
        except AuthException as e:
            return jsonify({}), e.error_code
        except HTTPException as e:
            common_res = {"rst": "err", "msg": "Bad Request", "err_code": e.code}
            log.error("Error %s" % str(e))
            log.error("Exception error: %s" % traceback.format_exc())
            return jsonify(common_res), BadRequest.code
        except ApiException as e:
            common_res = {"rst": "err", "msg": e.msg, "err_code": e.error_code}
            log.error("Error %s" % str(e))
            log.error("Exception error: %s" % traceback.format_exc())
            return jsonify(common_res), BadRequest.code
        except Exception as e:
            common_res = {"rst": "err", "msg": "系统响应失败", "err_code": 1000}
            log.error("Error %s" % str(e))
            log.error("Exception error: %s" % traceback.format_exc())
            return jsonify(common_res), InternalServerError.code

    return decorated_function
