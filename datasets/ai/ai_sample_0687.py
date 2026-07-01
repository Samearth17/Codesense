import smtplib 

# create SMTP object 
s = smtplib.SMTP('smtp-mail.outlook.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login("sender_address", "sender_password") 

# message to be sent 
message = """\
Subject: Hi there

This message is sent from Python."""

# sending the mail 
s.sendmail("sender_address", receivers_list , message) 

# terminating the session 
s.quit()