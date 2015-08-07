#! usr/bin/python
# -*- coding: utf-8 -*-
# rm_whitespace.py
# author: robot527
# created at 2015-8-5

'''
Remove trailing whitespaces in each line for code file.
'''

def file_travesal(directory='.', file_list=[]):
    '''
    Get file list from the directory including files in its subdirectories.
    '''
    from os import listdir
    from os.path import join, isfile, isdir
    file_list += [join(directory, f) for f in listdir(directory)
                if isfile(join(directory, f))]
    for item in listdir(directory):
        if isdir(join(directory, item)):
            file_travesal(join(directory, item), file_list)

def rm_whitespace(file_name):
    try:
        with open(file_name, 'r+') as code:
            line_list = [item.rstrip() + '\n' for item in code]
            code.seek(0)
            code.truncate(0)
            code.writelines(line_list)
            print 'Removed trailing whitespaces for file: ' + file_name
    except IOError as err:
        print 'File error: ' + str(err)


if __name__ == '__main__':
    print 'Please input a directory.'
    print 'Usage - "..", "/home/user/test/", default is "."'
    target_dir = raw_input("@> ")
    if target_dir is '':
        target_dir = '.'
    print 'Target directory is ' + target_dir + '  !\n'
    file_lst = []
    file_travesal(target_dir, file_lst)
    #Get .h file list
    h_file_list = [ef for ef in file_lst if ef[-2:] == '.h']
    #Get .c file list
    c_file_list = [ef for ef in file_lst if ef[-2:] == '.c']
    print '\t\t Total file number is %d !!!\n' % len(file_lst)
    for ef in h_file_list:
        rm_whitespace(ef)
    print
    for ef in c_file_list:
        rm_whitespace(ef)


