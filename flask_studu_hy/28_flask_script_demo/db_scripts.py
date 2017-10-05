#-*-coding:utf-8-*-

from flask_script import Manager

DBManager = Manager()

@DBManager.command
def init():
	print 'complete thr inital of database'



@DBManager.command
def migrate():
	print 'complete thr remigrate of database'





























