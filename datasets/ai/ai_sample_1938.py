import smtplib

# Email information
sender = 'user@example.com'
receivers = 'example@example.com'

message = """From: From User <user@example.com>
To: To User <example@example.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")