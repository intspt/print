#!/usr/bin/env python
#-*- coding:utf-8 -*-

from app import db

class Admin(db.Model):
	__tablename__ = 'admin'
	aid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(22))
	password = db.Column(db.String(22))

	def __init__(self, name, password):
		self.name = name
		self.password = password

	def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.uid)

class Team(db.Model):
	__tablename__ = 'team'
	tid = db.Column(db.Integer, primary_key=True)
	number = db.Column(db.Integer)
	location = db.Column(db.String(99))

	def __init__(self, number, location):
		self.number = number
		self.location = location

class Submit(db.Model):
	__tablename__ = 'submit'
	sid = db.Column(db.Integer, primary_key=True)
	team_number = db.Column(db.Integer)
	content = db.Column(db.Text)

	def __init__(self, team_number, content):
		self.team_number = team_number
		self.content = content