from flask import Flask, render_template, request, jsonify
import numpy as np
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('matrix_calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    expression = data['expression']

    # Parse matrices in the form of [[1,2];[3,4]] in the expression
    matrix_pattern = r'\[\[(.*?)\]\]' 
    matrix_count = 0
    matrix_vars = {}

    def replace_matrix(match):
        nonlocal matrix_count
        # Extract and format matrix from the match, e.g., "1,2;3,4" -> [[1, 2], [3, 4]]
        matrix_content = match.group(1)
        rows = matrix_content.split(';')
        matrix = [list(map(int, re.findall(r'-?\d+', row))) for row in rows]  # Use regex to find all integers
        matrix_var = f'matrix_{matrix_count}'
        matrix_vars[matrix_var] = np.array(matrix)
        matrix_count += 1
        return matrix_var

    # Replace all matrix patterns in the expression with variable names
    parsed_expression = re.sub(matrix_pattern, replace_matrix, expression)

    # Prepare for determinant and inverse operations
    parsed_expression = re.sub(r'det\((matrix_\d+)\)', r'np.linalg.det(\1)', parsed_expression)  # Handle determinant
    parsed_expression = re.sub(r'inv\((matrix_\d+)\)', r'np.linalg.inv(\1)', parsed_expression)  # Handle inverse

    # Check for validity and perform calculation
    try:
        # Make matrix variables available in the local namespace for eval
        local_vars = {var: matrix for var, matrix in matrix_vars.items()}
        
        # Perform the calculation using eval
        result_matrix = eval(parsed_expression, {"np": np}, local_vars)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    # Convert the result matrix to a list for JSON response
    return jsonify({"result_matrix": result_matrix.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
