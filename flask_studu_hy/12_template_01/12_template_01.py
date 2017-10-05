#-*-coding:utf-8-*-
from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
	class Person(object):
		name = u'朱华建'
		age = 18
	p = Person()

	context = {
		'username':u'123',
		'gender' : u'男',
		'age': 18,
		'person':p,
		'websites':{
			'baidu':'www.baidu.com',
			'google':'www.google.com'
		}

	}
	return render_template('index.html',**context)


if __name__ == '__main__':
	app.run(debug=True)

'''1.如何渲染模板：
	*模板放在template文件夹下
	*从flask中导入render_template函数
	*在视图函数中，使用‘render_template’函数，渲染模板。注意：只需要填写模板的名字，不需要填写template文件夹的路径
2.模板传参：
	*如果只有一个或者少量参数，直接写在‘render_remplate’函数中，添加关键字参数就可以了。
	*如果有多个参数的时候，那么可以先把所有的参数放在一个字典里，然后把字典当成关键字参数传递进去，这样代码更加方便管理。
3.在模板中，如果要使用一个变量，语法是：{{params}}	
4.访问模型中的属性或者字典，可以通过{{params。property}}{{params['age']}}'''



































































































