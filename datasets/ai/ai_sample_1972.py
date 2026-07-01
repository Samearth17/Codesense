from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "<form action='/save' method='POST'><input type='text' name='email'/><input type='submit’/></form>"

@app.route("/save", methods=["POST"])
def save():
    email = request.form["email"]
    # save the email address to your database
    return redirect("/")

if __name__ == "__main__":
    app.run()