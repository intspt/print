#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

SECRET_KEY = 'dark flame master'

BASE_DIR = os.getcwd()
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_DIR + os.sep + 'app' + os.sep + 'data' + os.sep + 'data.db'

LOGIN_INFO_ERROR = u'用户名或密码不正确'
PERMISSION_ERROR = u'权限不足'
SUBMIT_SECCESS_INFO = u'提交成功'

ADMIN_NAME = 'rikka'
ADMIN_PASSWORD = 'yuta'

color = []
problem_num = 0
balloon_list = []
sent_list = []
teams = []