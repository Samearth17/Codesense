import smtplib

# Get the list of customers and their emails
customers = {}

# Configure the SMTP client
smtp = smtplib.SMTP('smtp.example.com', 587)
smtp.starttls()
smtp.login('username', 'password')

# Loop through customers and send an email when their product is available
for customer, product in customers.items():
    if product_available(product):
        email_message = 'Dear {customer}, \n\nYour product has arrived and is now available to purchase. Please visit our website for more details. \n\nSincerely, \nThe Inventory Team'.format(customer=customer)

        # Send the email
        smtp.sendmail(from_address, customer, email_message)