#! /usr/bin/python
# encoding: utf-8


import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="rootpwd",\
    db="mysql")

cursor = db.cursor()

test = 'hehe'
addUser = "GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,ALTER\
    ON testDB.*\
    TO '%s'@'localhost'\
    IDENTIFIED BY 'pwd321'" % (test)

try:
    cursor.execute(addUser)
    db.commit()
    print "Added user 'hehe' succeed.\n"
except MySQLdb.MySQLError as err:
    db.rollback()
    print 'Some error occurred, added user failed!', err


def showUserInfo(usr=None):
    if usr:
        sql = "select host, user, password from user\
            where user = '%s'" % (usr)
    else:
        sql = """select host, user, password from user
            where host like '%host%'"""
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        print 'host        user    password'
        print '------------=======-----------'
    for row in results:
        host, user, passwd = row[0], row[1], row[2]
        print host, ' ', user, ' ', passwd 
    print

showUserInfo(test)

delUser = "delete from user where user = '%s'" % (test)

try:
    cursor.execute(delUser)
    db.commit()
    print "Deleted user 'hehe' succeed.\n"
except MySQLdb.MySQLError as err:
    db.rollback()
    print 'Some error occurred, deleted user failed!', err

showUserInfo()

db.close()
