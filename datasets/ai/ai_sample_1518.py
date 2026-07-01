def filter_emails(emails, valid_domains):
 filtered_emails = []
 for email in emails:
 domain = email.split('@')[1]
 if domain in valid_domains:
 filtered_emails.append(email)
 return filtered_emails

emails = [
 'jane@domain1.com',
 'john@domain2.com',
 'dave@domain3.com',
 'sarah@domain4.com'
]
valid_domains = ['domain1.com', 'domain2.com']

filtered_emails = filter_emails(emails, valid_domains)
print(filtered_emails) // ['jane@domain1.com', 'john@domain2.com']