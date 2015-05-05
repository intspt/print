#!/usr/bin/env python
#-*- coding:utf-8 -*-

from app import db
from app.models import User, Team, Submit

db.drop_all()
db.create_all()
db.session.add(User('rikka', 'yuta', True))
db.session.commit()
db.session.close()