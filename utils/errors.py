# -*- coding: utf-8 -*-
"""
    @ Author:
    @ E-Mail:
    @ Date:

"""
SYSTEM_ERROR = {"error_code": 1000, "message": "System response failure"}
PARAMS_ERROR = {"error_code": 1001, "message": "Params Error"}
PARAMS_EXCEPTION = {"error_code": 1002, "message": "Params Exception"}
API_EXCEPTION = {"error_code": 1003, "message": "API NOT FOUND OR NOT SUPPORT"}
DATA_EXIST_EXCEPTION = {"error_code": 1004, "message": "Data not Empty"}
REQUEST_OTHER_API_EXCEPTION = {"error_code": 1005, "message": "Request extend API Failed"}

DAG_EXCEPTION = {"error_code": 2001, "message": "DAG Checked Failed!"}
REFERENCE_ERROR = {"error_code": 2002, "message": "Reference exist!"}
WRITE_FILE_ERROR = {"error_code": 3001, "message": "Write File Failed!"}
DB_ERROR = {"error_code": 4001, "message": "DB Operations Failure"}

HAS_SUB_ELE_ERROR = {"error_code": 6001, "message": "The Object Has sub element"}
SYNC_ERROR = {"error_code": 8001, "message": "Synv ldap exception"}

INTERNAL_EXCEPTION = {"error_code": 9001, "message": "Service Api Error!"}


class ApiException(Exception):
    def __init__(self, msg, error_code=1001):
        self.error_code = error_code
        self.msg = msg


class AuthException(Exception):
    def __init__(self, msg, error_code=401):
        self.error_code = error_code
        self.msg = msg


class SyncException(Exception):
    def __init__(self, msg, error_code=8001):
        self.error_code = error_code
        self.msg = msg
        super(SyncException, self).__init__(msg, error_code)

    def __str__(self):
        return 'SyncException: %s: %s' % (self.error_code, self.msg)


class ParamsException(ApiException):
    def __init__(self, msg, error_code=1001):
        self.error_code = error_code
        self.msg = msg
        super(ParamsException, self).__init__(msg, error_code)

    def __str__(self):
        return 'ParamsException: %s: %s' % (self.error_code, self.msg)


class ReferenceException(ApiException):
    def __init__(self, msg, error_code=2002):
        self.error_code = error_code
        self.msg = msg
        super(ReferenceException, self).__init__(msg, error_code)

    def __str__(self):
        return 'REFERENCEException: %s: %s' % (self.error_code, self.msg)


class FileHandleException(ApiException):
    def __init__(self, msg, error_code=3001):
        self.error_code = error_code
        self.msg = msg
        super(FileHandleException, self).__init__(msg, error_code)

    def __str__(self):
        return 'FileHandleException: %s: %s' % (self.error_code, self.msg)


class DBHandleException(ApiException):
    def __init__(self, msg, error_code=4001):
        self.error_code = error_code
        self.msg = msg
        super(DBHandleException, self).__init__(msg, error_code)

    def __str__(self):
        return 'DBHandleException: %s: %s' % (self.error_code, self.msg)


class GitHandleException(ApiException):
    def __init__(self, msg, error_code=5001):
        self.error_code = error_code
        self.msg = msg
        super(GitHandleException, self).__init__(msg, error_code)

    def __str__(self):
        return 'GitHandleException: %s: %s' % (self.error_code, self.msg)
