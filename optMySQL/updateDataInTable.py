#! /usr/bin/python
# encoding: utf-8
""" Example code for update data in table on MySQL database."""


import MySQLdb

db = MySQLdb.connect(host="localhost", user="testuser", passwd="test123",\
    db="testDB")

cursor = db.cursor()

# create an SQL update statement
sql = "update book set book_author_id = book_author_id + 1000"

try:
    cursor.execute(sql)
    db.commit()
    print 'Update data succeed.'
except MySQLdb.MySQLError as err:
    print 'Some error occurred, update data failed!', err

db.close()
