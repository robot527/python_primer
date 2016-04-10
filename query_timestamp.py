#! /usr/bin/python
# -*- coding: utf-8 -*-
# query_timestamp.py
# author: robot527
# created at 2016-3-24

'''
Display the local date and time(human-readable format)
to the POSIX timestamp.
'''


import time


def show_date_time(timestamp=time.time()):
    '''
    Display the local date and time(human-readable format)
    to the POSIX timestamp. Defualt show the current date and time.
    '''
    from datetime import datetime
    print datetime.fromtimestamp(timestamp).isoformat(' ')


if __name__ == '__main__':
    running = True
    print '''Please input a timestamp, or Press Enter for current time,\
    or q for exit.'''
    while running:
        print 'Usage - "Press Enter", "1458000000", "2147483647", "q"'
        try:
            para = raw_input("@> ")
        except EOFError:
            print "If you want to quit, press Q key.\n"
            continue
        if para is '':
            show_date_time()
            print "Current timestamp is", time.time()
            print
        elif para is 'q':
            para = raw_input("Do you really want to exit ([y]/n)?")
            if para is not 'n':
            #if para not in ['n', "no"]:
                running = False
        else:
            try:
                show_date_time(int(para))
            except ValueError:
                print "Input para error !"
            print
    else:
        print 'You have exited successfully.'
