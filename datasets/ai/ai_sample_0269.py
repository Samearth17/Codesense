import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 

subject = "Your Subject"
body = "Your message here"
sender = "from@fromdomain.com"
receivers = ["to@todomain.com"]

msg = MIMEMultipart()
msg['from'] = sender
msg['To'] = ", ".join(receivers)
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("username", "password")
text = msg.as_string()
server.sendmail(sender, receivers, text)
server.quit()