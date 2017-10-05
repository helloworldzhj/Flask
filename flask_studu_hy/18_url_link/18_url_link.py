#-*-coding:utf-8-*-

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login/')
def login():
	return render_template('login.html')

if __name__ == '__main__':
	app.run(debug=True)


#url链接，使用url_for（视图函数名称）可以反转成url，
1.语法：url_for('static',filename='路径')
2.静态文件，flask会从‘static’文件夹中开始寻找，所以不需要再写‘static’这个路径了。
3.可以加载css文件，可以加载js文件，还有image文件
第一个：加载css文件
<link rel="stylesheet" href="{{ url_for('static',filename='css/index.css')}}">
第二个：加载js文件
<script src="{{ url_for('static',filename='js/index.js')}}"></script>
第三个：加载图片文件
<img src="{{url_for('static',filename='images/zhiliao.png')}}" alt="">


































































































