""" This a program which used to deal with
    the test file called "sketch.txt".
"""

import os
import sys
print( os.getcwd() )
#os.chdir( 'the dir which include the file sketch.txt' )

try:
    data = open( 'sketch.txt' ) #open( 'not_exist.txt' )
except FileNotFoundError: # or IOError
    print( 'open file failed!' )
    sys.exit();

for each_line  in data:
    try:
        ( role, spoken ) = each_line.split( ':', 1 )
        print( role, end = '' )
        print( ' said: ', end = '' )
        print( spoken, end = '' )
    except ValueError:
        pass

data.close()
