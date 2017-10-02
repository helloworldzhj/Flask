#-*-coding:utf-8-*-

from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
	return '784654654897'


if __name__ == '__main__':
	app.run()
#在这儿传入一个关键字参数，debug=True
#有两个好处1.程序出问题的时候在界面反馈错误2.每次修改python文件，程序会自动加载，不需要手动启动服务器。


















































