#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time

from app import app, db, lm
from flask import render_template
from flask.ext.login import current_user

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
def home():
	if current_user.is_authenticated():
		return render_template('admin.html')
	else:
		return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	pass

