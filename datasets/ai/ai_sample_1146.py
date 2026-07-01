#!/usr/bin/env python
 
import cgi
 
#Get form data
form = cgi.FieldStorage()
 
name = form.getvalue('name')
age = form.getvalue('age')

# Display the results
print "Content-type: text/html"
print
print "<html>"
print "<body>"
print "<p>Hi, %s! You are %s years old.</p>" % (name, age)
print "</body>"
print "</html>"