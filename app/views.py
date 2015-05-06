#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from functools import wraps

from flask import render_template, g, request, redirect
from flask.ext.login import current_user, login_user, logout_user

from app import app, db, lm
from models import User
from config import LOGIN_INFO_ERROR

def throw_exception(f):
    @wraps(f)
    def call(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception, e:
            print e
            return unicode(e)
    return call

@lm.user_loader
def load_user(userid):
    return User.query.get(userid)

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@throw_exception
def home():
    if current_user.is_authenticated() and current_user.is_admin():
        return render_template('admin.html')
    else:
        return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
@throw_exception
def login():
    if request.method == 'POST':
        name, password = request.form['name'], request.form['password']
        if name:
            user = User.query.filter_by(name=name).first()
            if user is not None and password == user.password:
                login_user(user, remember=True)
                return redirect('/')
            else:
                return LOGIN_INFO_ERROR
        else:
            return LOGIN_INFO_ERROR
    else:
	   return render_template('login.html')

@app.route('/logout')
@throw_exception
def logout():
    logout_user()
    return redirect('/')


@app.route('/list')
@throw_exception
def list():
    return render_template('list.html')

@app.route('/addTeam')
@throw_exception
def addTeam():
    return render_template('addteam.html')
