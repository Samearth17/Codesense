import re

def classify_email(subject, body):
    # Check the subject line for keywords
    flags = check_subject(subject)

    # Check the body for keywords
    if not flags:
        flags = check_body(body)

    # return flags
    return flags

def check_subject(subject):
    flags = []
    # Check for spam
    spam_keywords = ['***SPAM***', '***ADV***']
    for keyword in spam_keywords:
        if re.search(keyword, subject):
            flags.append('SPAM')
            break

    # Check for purchases
    purchase_keywords = ['order', 'purchase', 'shipping', 'payment']
    for keyword in purchase_keywords:
        if re.search(keyword, subject):
            flags.append('PURCHASE')
            break

    return flags

def check_body(body):
    flags = []
    # Check for offensive language
    offensive_words = ['crap', 'stupid', 'idiot', 'shut up']
    for word in offensive_words:
        if re.search(word, body):
            flags.append('OFFENSIVE')
            break

    # Check for marketing content
    marketing_keywords = ['buy now', 'limited time', 'special offer', 'free']
    for keyword in marketing_keywords:
        if re.search(keyword, body):
            flags.append('MARKETING')
            break

    return flags