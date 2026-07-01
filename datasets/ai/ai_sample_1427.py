import smtplib

sender = ‘sender@example.com’
receivers = ‘receiver@example.com’

message = “””
Subject: Sending Email using Python

This is a test e-mail message.
”””

try:
   smtpObj = smtplib.SMTP(‘localhost’)
   smtpObj.sendmail(sender, receivers, message)         
   print(“Successfully sent email”)
except SMTPException:
   print(“Error: unable to send email”)