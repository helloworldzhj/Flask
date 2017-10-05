#-*-coding:utf-8-*-

from flask import Flask,render_template

app = Flask(__name__)

#for遍历字典


@app.route('/')
def index():
	books = [
		{	'name':u'西游记',
			'auther':u'吴承恩',
			'price': u'109'
		},
		{
			'name':u'红楼梦',
			'auther':u'曹雪芹',
			'price': u'200'

		},
		{
			'name': u'水浒传',
			'auther': u'施耐庵',
			'price': u'150'
		},
		{
			'name': u'三国演义',
			'auther': u'罗贯中',
			'price': u'120'
		}
	]

	return render_template('index.html',books=books)


if __name__ == '__main__':
	app.run(debug = True)


#这边它会反馈一个错误，就是说hash之类的错误。
































































































