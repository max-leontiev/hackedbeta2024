from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)


class Matrix:
    all_matrices = {}
    matrix_count = 0

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        Matrix.matrix_count += 1
        self.id = Matrix.matrix_count
        Matrix.all_matrices[self.id] = self

    def as_form(self):
        return render_template("matrix_form.html", matrix=self)

    def update_internal_np_array(self, values_list):
        self.np_array = np.array(values_list)
        print(Matrix.all_matrices[self.id].np_array)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/create_matrix", methods=["POST"])
def create_matrix():
    try:
        mat = Matrix(int(request.form["rows"]), int(request.form["columns"]))
    except ValueError:
        return "Please enter valid integers for rows and columns.", 400
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
