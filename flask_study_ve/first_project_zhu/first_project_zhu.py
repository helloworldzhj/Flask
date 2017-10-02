#-*-coding:utf-8-*-

from flask import Flask#从框架中导入这个类

app = Flask(__name__)
#初始化一个Flask对象，需要传递一个参数
#1.方便flask框架去寻找资源
#2.方便flask插件比如flask-Sqlalchemy出现错误的时候号去寻找问题所在的位置

@app.route('/')
#@app.route这是一个装饰器
#@开头并且在函数的上面，说明是装饰器
#它的作用是做一个url与视图函数的映射
#也就是说以后我们127.0.0.1：5000/这一/的时候就会执行下面的这个函数，然后将结果返回给浏览器
def hello_world():
	return '这是我第一个flask项目'


if __name__ == '__main__':
#如果当前文件作为入口程序执行，那么就执行app。run
	app.run()
#启动一个应用服务器，来监听并接受用户的请求
#并且处于死循环的状态































