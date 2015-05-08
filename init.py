#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

from app import db
from app.models import User, Submit

if os.path.exists('app\\data\\data.db'):
    print 'delete old db file'
    os.remove('app\\data\\data.db')

print 'create new db file'
db.create_all()
print 'add admin'
db.session.add(User('rikka', 'yuta', True))
db.session.commit()
db.session.close()