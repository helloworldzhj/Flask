#-*-coding:utf-8-*-

from flask import Flask,session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)
#添加数据到session中
#操作session的时候，跟操作字典是一样的
#SECRET_KEY
@app.route('/')
def hello_world():
	session['username'] = 'zhiliao'
	#如果没有指定session的过期时间，她就会在浏览器关闭以后就过期
	session.permanent=True
	#过期时间为一个月
	return 'Hello World!'

@app.route('/get/')
def get():
	return session.get('username')

@app.route('/delete/')
def delete():
	print session.get('username')
	session.pop('username')
	print session.get('username')
	return 'success'

@app.route('/clear/')
def clear():
	print session.get('username')
	session.clear()
	print session.get('username')
	return 'success'

if __name__ == '__main__':
	app.run(debug=True)







































































































