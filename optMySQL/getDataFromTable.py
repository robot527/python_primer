#! /usr/bin/python
# encoding: utf-8
""" Example code for get data to table on MySQL database."""


import MySQLdb

db = MySQLdb.connect(host="localhost", user="testuser", passwd="test123",\
    db="testDB")

cursor = db.cursor()

# create an SQL select statement
sql = """select * from book where book_author_name='Mark Lutz'"""

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        bookid, booktile, author, press, date = row[0], row[1], row[3],\
            row[4], row[5]
        print "book_id = %d, title = %s, author = %s, press = %s, date = %s"\
            % (bookid, booktile, author, press, date)
    print 'Get data succeed.'
except MySQLdb.MySQLError as err:
    print 'Some error occurred, get data failed!', err

db.close()
