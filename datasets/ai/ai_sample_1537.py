import requests
import smtplib

THRESHOLD_TIME = 5 # In seconds
WEBSITE_URL = 'http://www.example.com'
FROM_EMAIL_ADDRESS = 'alert@example.com'
TO_EMAIL_ADDRESS = 'admin@example.com'

def main():
 response = requests.get(WEBSITE_URL)
 response_time = response.elapsed.total_seconds()
 if response_time > THRESHOLD_TIME:
 send_email_alert()

def send_email_alert():
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.starttls()
 server.login(FROM_EMAIL_ADDRESS, 'password')
 
 message = 'Website response time exceeded threshold'
 server.sendmail(FROM_EMAIL_ADDRESS, TO_EMAIL_ADDRESS, message)
 server.quit()

if __name__ == '__main__':
 main()