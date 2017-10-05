#-*-coding:utf-8-*-

from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search/')
def search():
	q =  request.args.get('q')
	return u'用户提交的查询参数是：%s' % q

#默认的视图函数只能使用get请求
#如果要使用post请求，就需要写明
@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form.get('username')
		password = request.form.get('password')
		print 'username:%s' % username
		print 'password:%s' % password
		return 'post request'

if __name__ == '__main__':
	app.run(debug=True)







































































































