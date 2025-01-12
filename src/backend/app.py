from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

from frontend.backend.app import app

app = Flask(__name__)
CORS(app)

# Database connection details
conn_params = {
    "host": "localhost",
    "database": "your_database_name",
    "user": "your_username",
    "password": "your_password"
}

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM your_table")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h1>Hello World</h1>", response.data)

    def test_predict_valid_data(self):
        data = {"key1": "value1", "key2": "value2"}  # Example data
        response = self.app.post('/predict', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('prediction', data)


    def test_predict_invalid_data(self):
        # Test with invalid data, if applicable to your prediction logic
        data = {"invalid": "data"} # Example invalid data
        response = self.app.post('/predict', data=json.dumps(data), content_type='application/json')
        # Assertions depend on your error handling (e.g., 400 Bad Request)
        # Example:
        self.assertEqual(response.status_code, 200)  # Or assert a different status code, like 400, if you have error handling.
        data = json.loads(response.data)
        self.assertIn('prediction', data)
