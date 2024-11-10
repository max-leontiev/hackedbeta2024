from flask import Flask, render_template, request, redirect
from matrix import Matrix
from operations import BinaryOperator, Multiplication

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", calculation=Matrix.calculation, 
                           result=Matrix.result)

@app.route("/create_matrix", methods=["POST"])
def create_matrix():
    try:
        rows = int(request.form["rows"])
        columns = int(request.form["columns"])
    except ValueError:
        return "Please enter valid integers for rows and columns.", 400

    if rows <= 0 or rows > 20 or columns <= 0 or columns > 20:
        return (
            "Please enter valid integers in the range [1, 20] for rows and columns.",
            400,
        )

    Matrix(rows, columns)
    return redirect("/")


@app.route("/create_binary_operator/<operator_name>", methods=["POST"])
def create_binary_operator(operator_name):
    if (
        len(Matrix.calculation) == 0 # can't start calculation with binary operator
        or isinstance(Matrix.calculation[-1], BinaryOperator) # can't have two binary operators in a row
    ): 
        return redirect("/")
    binary_operator_class = BinaryOperator.from_name(operator_name)
    if binary_operator_class is not None: # if valid operator name was provided, append the operator
        Matrix.calculation.append(binary_operator_class(len(Matrix.calculation)))
    return redirect("/")

@app.route("/binary_operator/<int:operator_ind>", methods=["POST"])
def binary_operator(operator_ind):
    # ensure operator_ind is not too large
    if operator_ind > len(Matrix.calculation) - 1:
        return redirect("/")
    binary_operator_class = BinaryOperator.from_symbol(request.form["operation_symbol"])
    # if valid operation symbol was inputted and it 
    # represents a different operation compared to the existing symbol,
    # update the operation
    if (
        binary_operator_class is not None 
        and binary_operator_class != type(Matrix.calculation[operator_ind])
    ):
        Matrix.calculation[operator_ind] = binary_operator_class(operator_ind)
    return redirect("/")

# Route to handle matrix input and display result
@app.route("/matrix/<int:matrix_ind>", methods=["POST"])
def matrix(matrix_ind: int):
    if matrix_ind > len(Matrix.calculation) - 1:
        return redirect("/")
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
                else:  # otherwise set it to 0
                    element = 0
            row.append(element)
        values.append(row)
    mat.update_internal_np_array(values)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
