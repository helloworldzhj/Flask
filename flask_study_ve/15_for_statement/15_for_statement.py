#-*-coding:utf-8-*-

from flask import Flask,render_template

app = Flask(__name__)

#for遍历字典


@app.route('/')
def index():
	user={'username':u'zhuhuajian',
		  'age':18
		  }
	websites = ['baidu.com','google.com']
	for k,v in user.items():
		print k
		print v
	for website in websites:
		print website
	return render_template('index.html',user=user,websites=websites)


if __name__ == '__main__':
	app.run(debug = True)

#字典的遍历，语法和python一样，可以使用items，keys，values，iteritems，iterkeys，itervalues。
#再讲一下列表的遍历，语法和python一样。




































































































