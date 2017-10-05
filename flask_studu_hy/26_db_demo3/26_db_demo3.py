#-*-coding:utf-8-*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

#用户表
# create table users(
# 	id int primery ke\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\y autoincrement,
# 	username varchar(100) not null
# )
#
# #文章表
# create table article(
# 	id int primary key autoincrment,
# 	title varchar(100) not null,
# 	content text not null
# 	author_id int,
# 	foreign key 'author_id' reference 'user.id'
# )
class User(db.Model):
	__tablename__='user'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	username = db.Column(db.String(100),nullable=False)

	# 如果表生成了，还想给它添加其他元素这是不可行的，比如说添加password这样的元素就不添加不了了


class Article(db.Model):
	__tablename__='article'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	title = db.Column(db.String(100),nullable=False)
	content = db.Column(db.Text,nullable=False)
	author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	author=db.relationship('User',backref=db.backref('articles'))

	#第一个参数是表的名字User

db.create_all()#让他运行到数据库中

@app.route('/')
def index():
	#
	# user1 = User(username='zhiliao')
	# db.session.add(user1)#这只是添加到事务当中
	# db.session.commit()#这样才把数据提交到数据库当中，


	# article = Article(title='aaa',content='bbb',author_id=1)
	# db.session.add(article)
	# db.session.commit()

	# 然后我就要在里面找文章标题为aaa的这个作者
	# article = Article.query.filter(Article.title=='aaa').first()
	# author_id = article.author_id
	# user = User.query.filter(User.id==author_id).first()
	# print 'username:%s' % user.username

	# article = Article(title='aaa',content='bbb')
	# article.author=User.query.filter(User.id==1).first()
	# db.session.add(article)
	# db.session.commit()

	# article = Article.query.filter(Article.title == 'aaa').first()
	# print 'username:%s' % article.author.username

	#我要找到zhiliao这个用户写过的所有文章，
	# article=Article(title='111',content='222',author_id=1)
	# db.session.add(article)
	# db.session.commit()

	user =User.query.filter(User.username=='zhiliao').first()
	result = user.articles
	for article in result:
		print '-'*10
		print(article.title)




	return 'index'
if __name__ == '__main__':
	app.run(debug=True)







































































































