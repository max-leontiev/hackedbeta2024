from flask import render_template
import numpy as np

class Matrix:
    calculation = []

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.ind = len(Matrix.calculation)
        self.np_array = None
        Matrix.calculation.append(self)

    def get_value_as_string(self, row, col):
        if self.np_array is not None:
            return str(self.np_array[row][col])
        else:
            return ''
    def as_form(self):
        return render_template("matrix_form.html", matrix=self)

    def update_internal_np_array(self, values_list):
        self.np_array = np.array(values_list)
        print(self.np_array)
