import email
from collections import defaultdict

# function to group emails by their subject
def group_emails(emails):
    # dictionary to store emails with same subject
    grouped_emails = defaultdict(list)

    # loop through emails
    for email in emails:
        # get subject
        subject = email.get('Subject', '')
        # add to dict
        grouped_emails[subject].append(email)

    # return grouped emails
    return grouped_emails

# function to merge emails with the same subject into one single email
def merge_emails(grouped_emails):
    merged_emails = []

    # loop through grouped emails
    for subject, emails in grouped_emails.items():
        # list to store all email bodies
        email_bodies = []

        # loop through emails in the group
        for email in emails:
            # get email body
            body = email.get_body()
            # add it to the list
            email_bodies.append(body)

        # combine the email bodies
        combined_body = "\n\n".join(email_bodies)

        # create new email
        merged_email = email.Address.new_message(subject, combined_body)

        # add the merged eail to the list
        merged_emails.append(merged_email)

    # return the merged emails
    return merged_emails