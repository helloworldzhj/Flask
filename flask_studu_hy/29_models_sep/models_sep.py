#-*-coding:utf-8-*-

from flask import Flask
from exts import db
from models import Article
import config

app = Flask(__name__)
db.init_app(app)
app.config.from_object(config)


@app.route('/')
def hello_world():
	return 'hello world'


if __name__ == '__main__':
	app.run(debug=True)







































































































