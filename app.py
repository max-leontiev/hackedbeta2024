# save this as app.py
from flask import Flask, request, render_template
from markupsafe import escape
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def read_form():
    # Get the form data as Python ImmutableDict datatype
    data = request.form
    
    ## Return the extracted information (escape it to be safe)
    return render_template("index.html", calculation=escape(data['calculation']))
