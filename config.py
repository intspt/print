#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

BASE_DIR = os.getcwd()
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + BASE_DIR + os.sep + 'data' + os.sep + 'data.db'