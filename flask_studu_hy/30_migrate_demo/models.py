#!/usr/bin/env python
#-*-coding:utf-8-*-

from exts import db

class Article(db.Model):
	__tablename__='article'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	title = db.Column(db.String(100),nullable=False)
	content = db.Column(db.Text,nullable=False)
	tags = db.Column(db.String(100),nullable=False)

#models里面的article数据模型要映射到数据库中





























