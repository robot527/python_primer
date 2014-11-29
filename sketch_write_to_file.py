""" This a program which used to deal with
    the test file called "sketch.txt".
    And then, write the data which disposed
    from sketch.txt to two target file.
"""

import os
import sys
print( os.getcwd() )
#os.chdir( 'the dir which include the file sketch.txt' )

try:
    data = open( 'sketch.txt' )
except FileNotFoundError:
    print( 'File not found in the current working directory!' )
    sys.exit();

man = []
other = []
    
for each_line  in data:
    try:
        ( role, spoken ) = each_line.split( ':', 1 )
        spoken = spoken.strip()
        if role == 'Man':
            man.append( spoken )
        elif role == 'Other Man':
            other.append( spoken )
    except ValueError:
        pass

data.close()

""" Using two “with” statements to rewrite
the code without the “finally” suite.
"""
try:
	with open( 'man_data.txt', 'w' ) as man_file:
		print( man, file = man_file )
	with open( 'other_data.txt', 'w' ) as other_file:
		print( other, file = other_file )
except IOError as err:
	print( 'File error: ' + str( err ) )
