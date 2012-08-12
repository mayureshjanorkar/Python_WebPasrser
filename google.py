#!/usr/bin/python

import urllib
str = urllib.urlopen("http://www.google.com")

print "Content-type:text/html\n\n"

#print "Content-type:text/plain\n\n"
print (str.read())
