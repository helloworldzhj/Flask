#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask import g

def login_log():
	print u'当前登录用户是%s' % g.username

def login_ip_log(ip):
	pass
	#print u'当前登录用户的IP地址为：%s' % g.ip






























