from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def evaluate_expression(matrices, operation):
    matrix_objects = {}
    for matrix_id, matrix in matrices.items():
        matrix_objects[matrix_id] = np.array(matrix, dtype=float)

    try:
        result = eval(operation, {}, matrix_objects)
        return result.tolist()
    except Exception as e:
        return str(e)

@app.route('/calculate', methods=['POST'])

def calculate():
    data = request.get_json()
    matrices = data.get('matrices')
    operation = data.get('operation')

    result = evaluate_expression(matrices, operation)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)