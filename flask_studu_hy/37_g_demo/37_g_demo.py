#-*-coding:utf-8-*-

from flask import Flask,g,render_template,request
from utils import login_log
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'index'

@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method =='GET':
		return render_template('login.html')
	else:
		username=request.form.get('username')
		password=request.form.get('password')
		if username == 'zhu' and password == 'hua':
			#就认为当前用户的用户名和密码正确
			g.username = 'zhuiliao'
			g.ip='xx'
			login_log()
			return u'恭喜登陆成功'
		else:
			return u'您的用户名或密码错误！'

if __name__ == '__main__':
	app.run(debug=True)






































































































