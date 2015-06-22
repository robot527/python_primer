#! /usr/bin/python
# encoding: utf-8
'''
List directory contents of the host,
default host is http://linux.linuxidc.com/ .
'''

from ftplib import FTP

host = 'linux.linuxidc.com' #cannot include http://
user = 'www.linuxidc.com'
passwd = 'www.linuxidc.com'

ftp = FTP(host, user, passwd)
ftp.cwd('/pub/2011/08/01/')
ftp.retrlines('LIST')

ftp.quit()

