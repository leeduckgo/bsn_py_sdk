#-*- coding:utf-8 -*-


from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


# 初始化flask应用
app = Flask(__name__)
app.config.from_object('config')

# # 初始化数据库
# db = SQLAlchemy(app)

from app import views
