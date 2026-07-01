import re

emails = [ "Mike@example.co    m" , "Jane#gmail.com", "Mason*yahoo.com"]
result = []

for email in emails:
 email = re.sub('[^A-Za-z0-9@.+-_]', '', email)
 email = email.replace(' ', '')
 if 'gmail' in email:
 email = email.replace('gmail', 'google')
 elif 'yahoo' in email:
 email = email.replace('yahoo', 'ymail')
 result.append(email)

print(result)