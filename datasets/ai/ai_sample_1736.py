import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email message content
template = "Dear {name}, thank you for signing up for our subscription! We just wanted to let you know that we'll be sending you emails with the latest news and offers so you can stay up to date with what we have going on. Don't forget to check out our website to learn more about our services. Thanks again for signing up! -  Team XYZ"

# Load customer names and email address from file
with open('customer_file.csv') as f:
    customers = f.readlines()

# Iterate through customers and send email
for customer in customers:
    name = customer.split(',')[0]
    email_address = customer.split(',')[1]

    # Create message
    message = MIMEMultipart()
    message['Subject'] = 'Thanks for signing up for our subscription!'
    message['From'] = 'Team XYZ <support@xyz.com>'
    message['To'] = email_address

    # Formatted message
    message.attach(MIMEText(template.format(name = name), 'plain'))

    # Connect to server and send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('username', 'password')
    server.send_message(message)