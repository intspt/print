#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from functools import wraps

from flask import render_template, g, request, redirect, flash
from flask.ext.login import current_user, login_user, logout_user, login_required

from app import app, db, lm
from models import User, Submit
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

@app.route('/', methods = ['GET', 'POST'])
@login_required
@throw_exception
def home():
    if current_user.is_admin:
        return render_template('admin.html')
    else:
        if request.method == 'GET':
            return render_template('index.html')
        else:
            submit = Submit(current_user.name, request.form['content'], get_now_time())
            db.session.add(submit)
            db.session.commit()
            db.session.close()
            flash(SUBMIT_SECCESS_INFO)
            return redirect('/')

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

@app.route('/submitList')
@admin_required
@throw_exception
def submit_list():
    submit_list = Submit.query.order_by(Submit.id_.desc())
    return render_template('submitList.html', submit_list=submit_list)

@app.route('/addUser', methods = ['GET', 'POST'])
@admin_required
@throw_exception
def add_user():
    if request.method == 'GET':
        return render_template('addUser.html')
    else:
        user_list = request.form['content'].split('\n')
        for user in user_list:
            name, password, location = user.split()
            db.session.add(User(name, password, location=location))
            db.session.commit()
            db.session.close()

        return redirect('/')

@app.route('/printCode')
@admin_required
@throw_exception
def print_code():
    submit = Submit.query.filter_by(id_=request.args['submitID']).first()
    user = User.query.filter_by(name=submit.user_name).first()
    content = submit.content.split('\n')
    name, location = user.name, user.location
    Submit.query.filter_by(id_=request.args['submitID']).update({'is_printed': True})
    db.session.commit()
    db.session.close()
    return render_template('printCode.html', name=name, location=location, content=[(i + 1, line) for (i, line) in enumerate(content)])

@app.route('/deleteUser')
@admin_required
@throw_exception  
def delete_user():
    user = User.query.get(request.args['uid'])
    db.session.delete(user)
    db.session.commit()
    db.session.close()
    return redirect('/userList')

@app.route('/userList')
@admin_required
@throw_exception
def user_list():
    user_list = User.query.all()
    return render_template('userList.html', user_list=user_list)

@app.route('/logout')
@login_required
@throw_exception
def logout():
    logout_user()
    return redirect('/')