from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the form to input n and m
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            n = int(request.form['n'])
            m = int(request.form['m'])
        except ValueError:
            return "Please enter valid integers for n and m.", 400

        return render_template('matrix_form.html', n=n, m=m)

    return render_template('index.html')

# Route to handle matrix input and display result
@app.route('/matrix', methods=['POST'])
def matrix():
    n = int(request.form['n'])
    m = int(request.form['m'])
    
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            element_name = f"element_{i}_{j}"
            element = int(request.form[element_name])
            row.append(element)
        matrix.append(row)

    return render_template('display_matrix.html', matrix=matrix)

if __name__ == '__main__':
    app.run(debug=True)
