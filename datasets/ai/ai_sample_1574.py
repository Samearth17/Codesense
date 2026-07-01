import re

class EmailParser:
 def __init__(self, email):
 self.email = email
 
 def parse_username(self):
 return re.search('(.*)@', self.email).group(1)
 
 def parse_domain(self):
 return re.search('@(.*)', self.email).group(1)

# Usage
parser = EmailParser("john@example.com")
print(parser.parse_username())
# john
print(parser.parse_domain())
# example.com