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


try:
    man_data = open( 'man_data.txt', 'w' )
    other_data = open( 'other_data.txt', 'w' )
    
    print( man, file = man_data )
    print( other, file = other_data )
    
except IOError:
    print( 'File error' )

finally: #the code in the finally suite always runs
    man_data.close() #Ensure that the file is closed
    other_data.close() #ditto
    

