#-*-coding:utf-8-*-
from flask import Flask,render_template,request,session,redirect,url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

@app.route('/')
def hello_world():
	print 'index'
	return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
	print 'login'
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form.get('username')
		password = request.form.get('password')
		if username == 'zhiliao' and password == '111111':
			session['username'] ='zhiliao'
			return u'登陆成功'
		else:
			return u'用户名和密码错误！'

@app.route('/edit/')
def edit():
	return render_template('edit.html')



	# if hasattr(g,'username'):
	# 	return render_template('edit.html')
	# else:
	# 	return redirect(url_for('login'))
	# 在请求之前执行的 before_request
	# before_request是在视图函数执行之前执行的
	# before_request这个函数只是一个装饰器，他可以把需要设置为钩子函数的代码放到视图函数执行之前来执行
@app.before_request
def my_before_request():
	if session.get('username'):
		g.username=session.get('username',username='zhiliao')


@app.context_processor
def my_context_processor():
	# username=session.get('username')
	# if username:
	# 	return {'username':username}
	return {'username':'111111'}

if __name__ == '__main__':
	app.run(debug=True)







































































































