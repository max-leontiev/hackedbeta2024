# save this as app.py
from flask import Flask, request, render_template
from markupsafe import escape
app = Flask(__name__)

calculation_history = []

@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template("index.html", calculation_history=calculation_history)

@app.route('/result', methods=['POST'])
def read_form():
    # Get the form data as Python ImmutableDict datatype
    data = request.form
    calculation_history.append(escape(data['calculation']))

    ## Return the extracted information (escape it to be safe)
    return render_template("index.html", calculation_history=calculation_history)
