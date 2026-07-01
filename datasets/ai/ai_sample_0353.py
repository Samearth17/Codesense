"""
Write a Python program to extract phone numbers from a given text.
"""

import re

def extract_phone_numbers(text):
    phone_numbers = []
    pattern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    regex = re.compile(pattern)
    matches = regex.finditer(text)
    for m in matches:
        phone_numbers.append(m.group())
    return phone_numbers

text = "This is a sample text. Mr. Smith's cell phone number is (123) 456-7890 and Mrs. Smith's phone number is (321) 234-5678."
print(extract_phone_numbers(text))