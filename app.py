from flask import Flask, render_template, request, redirect
from matrix import Matrix

app = Flask(__name__)
app.secret_key = 'secretkey'  # Necessary for flashing messages

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", calculation=Matrix.calculation)

@app.route("/create_matrix", methods=["POST"])
def create_matrix():
    try:
        rows = int(request.form["rows"])
        columns = int(request.form["columns"])
    except ValueError:
        return "Please enter valid integers for rows and columns.", 400
    
    if rows <= 0 or rows > 20 or columns <= 0 or columns > 20:
        return "Please enter valid integers in the range [1, 20] for rows and columns.", 400
        
    Matrix(rows, columns)
    return render_template("index.html", calculation=Matrix.calculation)

# Route to handle matrix input and display result
@app.route("/matrix/<int:matrix_ind>", methods=["POST"])
def matrix(matrix_ind: int):
    if matrix_ind > len(Matrix.calculation) - 1:
        return render_template("index.html", calculation=Matrix.calculation)
    mat = Matrix.calculation[matrix_ind]
    values = []
    for row_num in range(mat.rows):
        row = []
        for col_num in range(mat.columns):
            element_name = f"element_{row_num}_{col_num}"
            try:
                element = float(request.form[element_name])
            except ValueError:
                # default to old element if input is invalid and previous input exists
                if mat.np_array is not None:
                    element = Matrix.calculation[matrix_ind].np_array[row_num][col_num]
                else: # otherwise set it to 0
                    element = 0
            row.append(element)
        values.append(row)
    mat.update_internal_np_array(values)
    return render_template("index.html", calculation=Matrix.calculation)


if __name__ == "__main__":
    app.run(debug=True)
