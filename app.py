from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/homepage")
def homepage():
    render_template("homepage.html")