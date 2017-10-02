#!/usr/bin/env python
#-*-coding:utf-8-*-

DEBUG=True

#SECRET_KEY
#SQLALCHEMY_DB

#新建一个config。py文件
#在主app文件中导入这个配置文件，
import config
app.config.from_object(config)

其他还有许多参数都是放在这个配置文件中。
























