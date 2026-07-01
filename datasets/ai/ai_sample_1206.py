"""
Generate a Python script to scrub a list of emails for invalid entries
"""

import re

def validate_email(email):
    # Create the regex
    email_regex = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
    # Check whether the email is valid
    is_valid = email_regex.match(email)
    # Return the result
    return is_valid
    
def scrub_emails(emails):
    # Initialize a list for valid emails
    valid_emails = []
    # Loop over the emails and validate them
    for email in emails:
        # Check if the email is valid
        is_valid = validate_email(email)
        # If valid, append to the list
        if is_valid:
            valid_emails.append(email)
    # Return the list of valid emails
    return valid_emails