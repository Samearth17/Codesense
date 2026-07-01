<html>
<head>
    <title>Python Form Demo</title>
</head>
<body>
    <form method="post" action="/add">
        <input type="text" name="num1">
        <input type="text" name="num2">
        <input type="submit" value="Calculate">
    </form>
</body>
</html>

@app.route('/add', methods=['POST'])
def add():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 + num2
    return "The result of {} + {} is {}".format(num1, num2, result)