#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time

from app import app, db, lm
from flask import render_template, g, request, redirect
from flask.ext.login import current_user, login_user, logout_user
from models import User

@lm.user_loader
def load_user(userid):
    return User.query.get(userid)

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
def home():
    if current_user.is_authenticated() and current_user.is_admin():
        return render_template('admin.html')
    else:
        return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        print request.form['name'], request.form['password']
        if request.form['name'] != None and request.form['password'] != None:
            user = User.query.filter_by(name = request.form['name']).first()
            login_user(user)
            return redirect('/')
        else:
            return 'name and password must not be None!'
    else:
	   return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

