#! /usr/bin/python

def file_travesal(dirtectory='.', file_list=[]):
    '''
    Get file list from the directory including files in its subdirectories.
    '''
    from os import listdir
    from os.path import join, isfile, isdir
    file_list += [join(dirtectory, f) for f in listdir(dirtectory)
                if isfile(join(dirtectory, f))]
    for item in listdir(dirtectory):
        if isdir(join(dirtectory, item)):
            file_travesal(join(dirtectory, item), file_list)

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
    for each_item in file_lst:
        print each_item
    print '\t\t Total file number is %d !!!\n' % len(file_lst)
    print h_file_list
    print
    print c_file_list
