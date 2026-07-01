import smtplib

sender_email = "sender@gmail.com"
receiver_email = "receiver@example.com"
password = 'password'

message = """\
Subject: Hi There

This is an email to test the Gmail SMTP service.
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)

server.quit()