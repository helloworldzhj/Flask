#-*-coding:utf-8-*-
#存放项目的配置
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME='127.0.0.1'
PORT	='3306'
DATABASE='zlktqa_demo'
USERNAME='root'
PASSWORD='password'
DB_URI	='mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False



























