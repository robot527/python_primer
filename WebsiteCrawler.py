#! /usr/bin/python2.7
import re
import urllib


#The preferred way to open a file is with the builtin open() function.
textfile = open('depth_1.txt', 'wt')
print "Enter the URL you wish to crawl.."
print 'Usage - "http://phocks.org/stumble/creepy/" <-- With the double quotes'
myurl = input("@> ")
"""
findall(pattern, string, flags=0)
    Return a list of all non-overlapping matches in the string.
urlopen(url, data=None, proxies=None)
    Create a file-like object for the specified URL to read from.
re.I is an abbreviation of re.IGNORECASE
"""
for i in re.findall('''href=["'](.[^"']+)["']''',\
                    urllib.urlopen(myurl).read(), re.I):
    print i
    for ee in re.findall('''href=["'](.[^"']+)["']''',\
                        urllib.urlopen(i).read(), re.I):
        print ee
        textfile.write(ee+'\n')
textfile.close()
