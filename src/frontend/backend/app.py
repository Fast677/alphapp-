import unittest

if __name__ == '__main__':
    unittest.main()

from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Process the data and make predictions here
    prediction = {'prediction': 'This is a sample prediction'}
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
