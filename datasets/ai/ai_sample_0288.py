import re

html = "<div class=\"data\"> \
 <h1>Name: John Doe</h1> \
 <h3>Age: 25</h3> \
 <h3>Location: Los Angeles, CA</h3> \
</div>"

pattern = '<h1>Name: (.*)</h1>.*<h3>Age: (.*)</h3>.*<h3>Location: (.*)</h3>'

data = re.search(pattern, html)

name = data.group(1)
age = data.group(2)
location = data.group(3)

print('Name: {}'.format(name))
print('Age: {}'.format(age))
print('Location: {}'.format(location))