""" This a program which used to deal with
    the test file called "sketch.txt".
    And then, write the data which disposed
    from sketch.txt to two target file.
"""

import os
import sys
print(os.getcwd())
#os.chdir('the directory which include the file sketch.txt')

try:
    data = open('sketch.txt')
except FileNotFoundError:
    print('File not found in the current working directory!')
    sys.exit();
man = []
other = []


def print_nested_list_V3(alist, indent=False, level=0, fh=sys.stdout):
    """ This function takes one positional argument call "alist" which is
        any Python list (of possibly nested list), and two optional arguments
        called "indent" and "level". The indent controls print style, False
        means disable indent, True means enable indent. The level controls
        the amount of indentation for each item in in the provided list.
        Each data item in the provided list is (recursively) printed to the
        screen on it's own line. Added a fourth argument "fh" with a default
        value to print_nested_list_V2() function to identify a place to write
        data to.
    """
    for item in alist:
        if isinstance(item, list):
            print_nested_list_V3(item, indent, level + 1, fh)
        else:
            if indent:
                print('\t' * level, end='', file=fh)
            print(item, file=fh)

for each_line  in data:
    try:
        (role, spoken) = each_line.split(':', 1)
        spoken = spoken.strip()
        if role == 'Man':
            man.append(spoken)
        elif role == 'Other Man':
            other.append(spoken)
    except ValueError:
        pass

data.close()

""" Using two “with” statements to rewrite
the code without the “finally” suite.
"""
try:
	with open('man_data.txt', 'w') as man_file:
		print_nested_list_V3(man, False, 0, man_file)
	with open('other_data.txt', 'w') as other_file:
		print_nested_list_V3(other, fh=other_file)
except IOError as err:
	print('File error: ' + str(err))
