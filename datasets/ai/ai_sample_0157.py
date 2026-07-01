from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        return render_template('result.html', input_text=input_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

// result.html file
<html>
 <body>
  <h1>Your Input: </h1>
  <p>{{input_text}}</p>
 </body>
</html>