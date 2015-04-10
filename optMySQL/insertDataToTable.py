#! /usr/bin/python
# encoding: utf-8
""" Example code for insert data to table on MySQL database."""


import MySQLdb

# create a connection to the MySQL server
db = MySQLdb.connect(host="localhost", user="testuser", passwd="test123",\
    db="testDB")

cursor = db.cursor()

# create an SQL insert statement
sql = """INSERT INTO book(book_id,
        book_title, book_author_id,
        book_author_name, press, publication_date)
        values(1, 'Head First Python', 1, 'Paul Barry',
        "O'Reilly", '2010-12-07')"""

try:
    cursor.execute(sql)
    # commit data to db
    db.commit()
    print 'Inserted data succeed.'
except MySQLdb.MySQLError as err:
    # Rollback in case there is any error
    db.rollback()
    print 'Some error occurred, insert data failed!', err

db.close()
