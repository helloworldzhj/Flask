#-*-coding:utf-8-*-
#专门用来写命令的文件

from flask_script import Manager#在终端写的类似脚本的
from flask_migrate import Migrate,MigrateCommand#做模型到表的一个迁移需要用到这个模块
from zlktqa import app#manage的初始化需要用到我们的那个app
from exts import db
from models import User,Question,Answer

manager = Manager(app)

#使用Migrate绑定app和db，所以上面还要导入db
migrate = Migrate(app,db)

#添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)#把所有的子命令绑定到db上
#那我们的这个MigrateCommand就会去读取我们导入进来的这个模型


if __name__ == '__main__':
	manager.run()





















