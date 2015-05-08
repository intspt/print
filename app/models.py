#!/usr/bin/env python
#-*- coding:utf-8 -*-

from app import db

class User(db.Model):
    __tablename__ = 'user'
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(22))
    password = db.Column(db.String(22))
    is_admin = db.Column(db.Boolean)
    location = db.Column(db.String(99))

    def __init__(self, name, password, is_admin=False, location=''):
        self.name = name
        self.password = password
        self.is_admin = is_admin
        self.location = location

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id_)

class Submit(db.Model):
    __tablename__ = 'submit'
    id_ = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Integer)
    content = db.Column(db.Text)
    time_ = db.Column(db.String(9))
    is_printed = db.Column(db.Boolean)

    def __init__(self, user_name, content, time_, is_printed=False):
        self.user_name = user_name
        self.content = content
        self.time_ = time_
        self.is_printed = is_printed