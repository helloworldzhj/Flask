#!/usr/bin/env python
#-*-coding:utf-8-*-

# dialect+driver://username:password@host:port/database

DIALECT='mysql'
DRIVER='mysqldb'
USERNAME='root'
PASSWORD='password'
HOST='127.0.0.1'
PORT='3306'
DATABASE='db_demo1'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

#这边的主要内容是数据库和flask的连接
使用flask_sqlalchemy中的sqlalchemy进行初始化
在配置文件config.py中配置信息
再导入我们自己设置的config配置信息内容
做测试看看有没有错。
如果没有报错说明配置没问题























