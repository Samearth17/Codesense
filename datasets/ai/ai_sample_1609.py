def email_classification(email):
    email_type = ""
    if 'ShippingConfirmation' in email:
        email_type = 'Shipping Confirmation'
    elif 'Subscriber' in email:
        email_type = 'Subscriber'
    elif 'CommentResponse' in email:
        email_type = 'Comment Response'
    else:
        email_type = 'Unknown'

    return email_type

emails = [
    'ShippingConfirmation@example.com', 
    'Subscriber@example.com', 
    'CommentResponse@example.com'
]

for email in emails:
    print(email_classification(email))