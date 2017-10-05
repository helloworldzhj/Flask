#-*-coding:utf-8-*-

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
	comments = [
		{
			'user':u'黄勇',
			'content':'xxxx'
		},
		{
			'user':u'知了课堂',
			'content':'xxxx'
		}
	]
	return render_template('index.html',comments=comments)


if __name__ == '__main__':
	app.run(debug=True)

#过滤器可以处理变量，把原始的变量经过处理后再展示出来
'''
{{ avatar|default('***') }}
也就是说当我们当前这个变量不存在的时候我们就有替代它的东西出现

fefault过滤器：如果当前变量不存在我们就可以指定默认值
length：过滤器'''





































































































