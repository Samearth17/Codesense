import smtplib

sender_email = 'example@gmail.com'
password = 'example_password'

for email in recipient_emails:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)

        subject = 'Automated Email from Program'
        message = 'Message body'
 
        server.sendmail(sender_email, email, 'Subject: ' + subject + '\n\n' + message)
        server.quit()
        print('Email sent successfully.')