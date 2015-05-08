#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

SECRET_KEY = 'dark flame master'

BASE_DIR = os.getcwd()
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_DIR + '\\app\\data\\data.db'

LOGIN_INFO_ERROR = '用户名或密码不正确'
PERMISSION_ERROR = '权限不足'
SUBMIT_SECCESS_INFO = '提交成功'