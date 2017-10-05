#-*-coding:utf-8-*-

from flask_script import Manager
from flask_script_demo import app
from db_scripts import DBManager

manager = Manager(app)




@manager.command
def runserver():
	print 'the server is running!!!!'

manager.add_command('db',DBManager)



if __name__=='__main__':
	manager.run()































