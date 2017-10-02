#-*-coding:utf-8-*-

from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
	login_url = url_for('login')
	return redirect('/login/')
	return u'这是首页'

@app.route('/login/')
def login():
	return u'这是登陆页面'

@app.route('/question/<is_login>/')
def question(is_login):
	if is_login=='1':
		return u'这是发布问答页面'
	else:
		return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)

#页面跳转和重定向
1.用处：在用户访问一些需要登陆的页面的时候，如果用户没有登录，就重定向到登录界面，如果登陆了，就跳转到问答界面





































































































