from flask import Flask
app = Flask(__name__)
//Jiratest

@app.route("/")
def index():
    return "<h1>Hello Azure!</h1>"
