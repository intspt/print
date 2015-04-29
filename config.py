#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

SECRET_KEY = 'dark flame master'

BASE_DIR = os.getcwd()
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + BASE_DIR + os.sep + 'app' + os.sep + 'data' + os.sep + 'data.db'
