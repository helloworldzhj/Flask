#-*-coding:utf-8-*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)

db =SQLAlchemy(app)

class Article(db.Model):
	__tablename__='article'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	title = db.Column(db.String(100),nullable=False)
	content = db.Column(db.Text,nullable=False)
db.create_all()

@app.route('/')
def hello_world():
	#增
	# article1 = Article(title='aaa',content = 'bbb')#增加
	# db.session.add(article1)
	# db.session.commit()#事务

	#查
	# select * from article wher title='aaa':
	# result = Article.query.filter(Article.title=='aaa').first()
	# print 'title:%s' % result.title
	# print 'content:%s' % result.content

	#改：
	# 1.查找出要改的数据
	# article1= Article.query.filter(Article.title=='aaa').first()
	# 2.把需要修改的地方进行修改
	# article1.title='new title'
	# 3.做事务进行提交
	# db.session.commit()

	#删：
	#1.把需要删除的数据查找出来
	article1 = Article.query.filter(Article.content=='bbb').first()
	#2.把这条数据删除掉
	db.session.delete(article1)
	#3.做事务提交
	db.session.commit()



	return 'hello world!'

if __name__ == '__main__':
	app.run(debug=True)



































































































