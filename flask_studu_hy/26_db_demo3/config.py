#-*-coding:utf-8-*-

HOSTNAME='127.0.0.1'
PORT='3306'
DATABASE='db_demo3'
USERNAME='root'
PASSWORD='password'
DB_URI='mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True































