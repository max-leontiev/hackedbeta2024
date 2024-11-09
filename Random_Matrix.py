from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def index():
    return app.send_static_file('index.html')

@app.route('/generate_random_matrix', methods=['POST'])

def generate_random_matrix():
    data = request.get_json()
    rows = data.get('rows')
    cols = data.get('cols')

    if rows and cols:
        random_matrix = np.random.uniform(1, 1000, size=(rows, cols))

        result = random_matrix.tolist()

        return jsonify({'matrix': result})

if __name__ == '__main__':
    app.run(debug=True)