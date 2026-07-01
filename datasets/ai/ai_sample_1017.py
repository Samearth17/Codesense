import re

# strip whitespace
def strip_whitespace(s):
 return s.strip()

# remove HTML tags
def remove_html_tags(s):
 return re.sub('<[^>]*>', '', s)

# remove special characters
def remove_special_chars(s):
 return re.sub('[^\w\s]', '', s)

# convert ASCII characters to unicode characters
def convert_ascii_to_unicode(s):
 return s.encode('unicode-escape').decode('utf-8')

# convert strings to lowercase
def to_lower(s):
 return s.lower()

# sanitize user input
def sanitize_string(s):
 s = strip_whitespace(s)
 s = remove_html_tags(s)
 s = remove_special_chars(s)
 s = convert_ascii_to_unicode(s)
 s = to_lower(s)
 return s

# Example
my_string = '<Strin>G &#3238; !@#$%^'
my_string = sanitize_string(my_string)
print(my_string)