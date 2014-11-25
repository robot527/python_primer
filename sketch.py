""" This a program which used to deal with
    the test file called "sketch.txt".
"""

import os
print( os.getcwd() )
#os.chdir( 'the dir which include the file sketch.txt' )

data = open( 'sketch.txt' )

for each_line  in data:
    if not each_line.find( ':' ) == -1: #use key word "not"
        ( role, spoken ) = each_line.split( ':', 1 )
        print( role, end = '' )
        print( ' said: ', end = '' )
        print( spoken, end = '' )

data.close()
