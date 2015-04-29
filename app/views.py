#!/usr/bin/env python
#-*- coding:utf-8 -*-

from app import app, db, lm
from flask import render_template

@app.route('/')
def home():
	return render_template('index.html')