from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import re

app = Flask(__name__)
app.secret_key = 'secretkey'  # Necessary for flashing messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the expression entered by the user
        expression = request.form['expression']
        
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

        # Try to evaluate the expression
        try:
            # Replace matrix_var names in the parsed expression with actual matrix references
            for var, matrix in matrix_vars.items():
                exec(f"{var} = matrix_vars['{var}']")

            result_matrix = eval(parsed_expression)
        except Exception as e:
            flash(f"Error: {str(e)}", 'error')
            return render_template('matrix_calculator.html', expression=expression)
        
        return render_template('matrix_calculator.html', expression=expression, result_matrix=result_matrix.tolist())

    return render_template('matrix_calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
