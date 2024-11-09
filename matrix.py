from flask import render_template
import numpy as np

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
