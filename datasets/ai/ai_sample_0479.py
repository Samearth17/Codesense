import re

html_str = """
<html>
<head>
  <title>Page title</title>
</head>
<body>
  <p>For more information email us at info@example.com.</p>
  <p>You can also contact john@example.com.</p>
</body>
</html>"""

emails = re.findall(r'\S+@\S+', html_str)
print(emails)

# Output: ['info@example.com', 'john@example.com']