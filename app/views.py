#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from functools import wraps

from flask import render_template, g, request, redirect, flash
from flask.ext.login import current_user, login_user, logout_user

from app import app, db, lm
from models import User, Submit, Team
from config import LOGIN_INFO_ERROR, PERMISSION_ERROR, SUBMIT_SECCESS_INFO

def get_now_time():
    return time.strftime('%H:%M:%S',time.localtime(time.time()))

def admin_required(func):
    @wraps(func)
    def check(**args):
        if current_user.is_authenticated() and current_user.is_admin:
            return func(**args)
        else:
            return PERMISSION_ERROR
    return check

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
@login_required
@throw_exception
def home():
    if current_user.is_authenticated() and current_user.is_admin():
        return render_template('admin.html')
    else:
        return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
@throw_exception
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
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

@app.route('/printCode', methods = ['GET', 'POST'])
@login_required
@throw_exception
def print_code():
    if request.method == 'GET':
        return render_template('printCode.html')
    else:
        submit = Submit(team_number=current_user.number, content=request.form['content'], time=get_now_time())
        db.session.add(submit)
        db.session.commit()
        db.session.close()
        flash(SUBMIT_SECCESS_INFO)
        return redirect('/')

@app.route('/submitList')
@admin_required
@throw_exception
def submit_list():
    submit_list = Submit.query.order_by('submit.sid DESC')
    return render_template('list.html', submit_list=submit_list)

@app.route('/addTeam', methods = ['GET', 'POST'])
@admin_required
@throw_exception
def add_team():
    if request.method == 'GET':
        return render_template('addteam.html')
    else:
        team_list = request.form['teamList'].split('\n')
        print team_list
        return redirect('/')

@app.route('/teamList')
@admin_required
@throw_exception
def team_list():
    pass

@app.route('/logout')
@login_required
@throw_exception
def logout():
    logout_user()
    return redirect('/')