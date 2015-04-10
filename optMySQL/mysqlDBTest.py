#! /usr/bin/python
# encoding: utf-8
""" Sample code for connecting MySQL database."""


import MySQLdb

# 连接数据库
db = MySQLdb.connect("localhost", "testuser", "test123")

# 使用 cursor() 方法获取操作游标
cursor = db.cursor()

# 使用execute() 方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条记录
data = cursor.fetchone()

print "MySQL database version : %s " % data

# 关闭数据库连接
db.close()
