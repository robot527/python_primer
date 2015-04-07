#! /usr/bin/python3
""" This is the "nester.py" module and id provides two function called
  print_nested_list() and print_nested_list_V2() which print lists
  that may or may not include nested lists.
"""


def print_nested_list(alist, indent=False, level=-1):
    """print Python list (of possibly nested list)"""
    if True == isinstance(alist, list):
        for item in alist:
            print_nested_list(item, indent, level + 1)
    else:
        if indent:
            for tab_stop in range(level):
                print("\t", end='') #print a TAB for indent
        print(alist)


def print_nested_list_V2(alist, indent=False, level=0):
    """ This function takes one positional argument call "alist" which is
        any Python list (of possibly nested list), and two optional arguments
        called "indent" and "level". The indent controls print style, False
        means disable indent, True means enable indent. The level controls
        the amount of indentation for each item in in the provided list.
        Each data item in the provided list is (recursively) printed to the
        screen on it's own line.
    """
    for item in alist:
        if isinstance(item, list):
            print_nested_list_V2(item, indent, level + 1)
        else:
            if indent:
                print('\t' * level, end='')
            print(item)



test_list = [
    'The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91,
    [
        'Graham Chapman',
        ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
    ],
    'added by robot527',
    [21, 32, 55],
    (2, 3, 4),
    [1.23, ['float', 'double']],
    "python 3.4.2"
    ]

#test code
print(test_list)
print('\n')

print_nested_list(test_list)
print('\n')

print_nested_list_V2(test_list, True)
print('\n')

print_nested_list_V2(test_list, True, 2)
print('\n')
