""" This a program which used to deal with
    the test file called "sketch.txt".
"""

import os
import sys
print( os.getcwd() )
#os.chdir( 'the dir which include the file sketch.txt' )

try:
    data = open( 'sketch.txt' ) #open( 'not_exist.txt' )
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

print( man )
print( other )
