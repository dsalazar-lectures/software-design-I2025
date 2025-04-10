from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route('/<name>')
def hello_world(name=None):
    return render_template('hello.html', person=name)