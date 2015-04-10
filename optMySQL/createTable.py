#! /usr/bin/python
# encoding: utf-8
""" Example code for create table on MySQL database."""


import MySQLdb

# 连接数据库
db = MySQLdb.connect("localhost", "testuser", "test123", "testDB")

# 使用 cursor() 方法获取操作游标
cursor = db.cursor()

# 组织创建数据表SQL语句
sql = """CREATE TABLE book(
        book_id INT NOT NULL AUTO_INCREMENT,
        book_title VARCHAR(100) NOT NULL,
        book_author_id INT NOT NULL,
        book_author_name VARCHAR(40) NOT NULL, 
        press VARCHAR(100) NOT NULL,
        publication_date DATE,
        PRIMARY KEY (book_id)
        )"""

# 执行SQL语句
cursor.execute(sql)

db.close()
