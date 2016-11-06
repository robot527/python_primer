#! /usr/bin/python
# -*- coding: utf-8 -*-
# rm_whitespace_for_file.py
# author: robot527
# created at 2016-11-6

'''
Remove trailing whitespaces in each line for specified file.
'''


def rm_whitespace(file_name):
    '''Remove trailing whitespaces for a text file.'''
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
    import sys
    argc = len(sys.argv)
    if argc < 2:
        print 'Usage: python rm_whitespace_for_file.py /path/to/file'
    else:
        rm_whitespace(sys.argv[1])
