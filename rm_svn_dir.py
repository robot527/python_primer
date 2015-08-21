#! /usr/bin/python
# -*- coding: utf-8 -*-
# rm_svn_dir.py
# author: robot527
# created at 2015-8-19

def get_svn_list(directory='.', dir_list=[]):
    '''
    Get .svn list from directory.
    '''
    from os import listdir
    from os.path import join, isdir
    dir_list += [join(directory, d) for d in listdir(directory)
                if isdir(join(directory, d)) and d == '.svn']
    for item in listdir(directory):
        if isdir(join(directory, item)):
            get_svn_list(join(directory, item), dir_list)


if __name__ == '__main__':
    from os import system
    print 'Please input a directory.'
    print 'Usage - "..", "/home/user/test/", default is "."'
    target_dir = raw_input("@> ")
    if target_dir is '':
        target_dir = '.'
    print 'Target directory is ' + target_dir + '  !\n'
    dir_lst = []
    get_svn_list(target_dir, dir_lst)
    if dir_lst == []:
        print "Can't find .svn in target directory!"
    else:
        for each in dir_lst:
            print each
            cmd = 'rm -rf ' + each
            system(cmd)
