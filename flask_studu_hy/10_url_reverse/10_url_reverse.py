#-*-coding:utf-8-*-

from flask import Flask,url_for

app = Flask(__name__)


@app.route('/')
def index():
	print url_for('my_list')
	print url_for('article',id='abc')
	return 'Hello World!'

@app.route('/list/')
def my_list():
	return 'list'

@app.route('/article/<id>/')
def article():
	return u'您的请求id是：%s' % id

if __name__ == '__main__':
	app.run(debug=True)

#这样就从视图函数到url的转换叫做反转url
#在页面重定向的时候，会使用反转url
在模板中也会使用url反转




































































































