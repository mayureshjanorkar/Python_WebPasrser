#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('t1')

print "Content-type:text/html\n\n"
#print "Content-type:text/plain\n\n"

print '<html>'
print '<head>'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print '<h4>Hello Word! This is my first CGI program</h4>'

print '<br><br>'
print '<h2>Hello %s </h2>' % (first_name)
print '<br><br>'

print '<a href="http://cs-server.usc.edu:10101/cgi-bin/movie.py">Movies</a>'
print '<br><br>'

print '<a href="http://cs-server.usc.edu:10101/cgi-bin/google.py">Google</a>'
print '<br><br>'

print '<a href="http://cs-server.usc.edu:10101/first.html">Back</a>'

print '</body>'
print '</html>'
