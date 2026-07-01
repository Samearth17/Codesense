#!/usr/bin/python

import os

# Install Apache Web Server
os.system('sudo apt-get install apache2')

# Install MySQL server
os.system('sudo apt-get install mysql-server')

# Create database
os.system('mysql -u root -p create database mydb')

# Create user
os.system('mysql -u root -p grant all privileges on mydb.* to username@localhost identified by 'password';

# Copy html file
html_file='index.html'
os.system('cp ' + html_file + ' /var/www/html/')

# Create and run CGI script
cgi_file='my_cgi.py'
os.system('cp ' + cgi_file + ' /usr/lib/cgi-bin/')
os.system('sudo chmod 755 /usr/lib/cgi-bin/'+cgi_file)

# Create connection file
conn_file='my_conn.py'
os.system('cp ' + conn_file + ' /usr/lib/')