#-*-coding:utf-8-*-

from functools import wraps
from flask import session,redirect,url_for

def login_required(func):#登陆限制的装饰器
	@wraps(func)
	def wrapper(*args,**kwargs):
		if session.get('user_id'):
			return func(*args,**kwargs)
		else:
			return redirect(url_for('login'))
	return wrapper































