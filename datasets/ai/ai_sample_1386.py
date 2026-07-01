from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
 if request.method == 'POST':
 number = int(request.form['number'])
 incremented_number = number + 1
 return render_template('index.html', incremented_number=incremented_number)
 else:
 return render_template('index.html')

if __name__ == '__main__':
 app.run(debug=True)

<!DOCTYPE html>
<html>
<head>
 <title>Python Flask Example</title>
</head>
<body>
	<form method="post">
		<input type="number" name="number" />
		<input type="submit" value="Submit" />
	</form>
	
	{% if incremented_number %}
		<p>{{ incremented_number }}</p>
	{% endif %}
</body>
</html>