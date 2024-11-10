from flask import Flask, render_template, request
from matrix import Matrix

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/create_matrix", methods=["POST"])
def create_matrix():
    try:
        rows = int(request.form["rows"])
        columns = int(request.form["columns"])
    except ValueError:
        return "Please enter valid integers for rows and columns.", 400
    
    if rows <= 0 or rows > 20 or columns <= 0 or columns > 20:
        return "Please enter valid integers in the range [1, 20] for rows and columns.", 400
        
    mat = Matrix(rows, columns)
    return mat.as_form()

# Route to handle matrix input and display result
@app.route("/matrix/<int:matrix_id>", methods=["POST"])
def matrix(matrix_id: int):
    mat = Matrix.all_matrices[matrix_id]
    values = []
    for row_num in range(mat.rows):
        row = []
        for col_num in range(mat.columns):
            element_name = f"element_{row_num}_{col_num}"
            element = int(request.form[element_name])
            row.append(element)
        values.append(row)
    Matrix.all_matrices[matrix_id].update_internal_np_array(values)

    return Matrix.all_matrices[matrix_id].as_form()


if __name__ == "__main__":
    app.run(debug=True)
