from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Database connection details
conn_params = {
    "host": "localhost",
    "database": "your_database_name",
    "user": "your_username",
    "password": "your_password"
}

def get_db_connection():
    conn = psycopg2.connect(**conn_params, cursor_factory=RealDictCursor)
    return conn

@app.route('/api/v1/resource', methods=['GET'])
def get_resources():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    offset = (page - 1) * limit

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM resources LIMIT %s OFFSET %s', (limit, offset))
    resources = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(resources)

@app.route('/api/v1/resource', methods=['POST'])
def create_resource():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO resources (name, description) VALUES (%s, %s) RETURNING *', (name, description))
    new_resource = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(new_resource), 201

@app.route('/api/v1/resource/<int:id>', methods=['PUT'])
def update_resource(id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE resources SET name = %s, description = %s WHERE id = %s RETURNING *', (name, description, id))
    updated_resource = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if updated_resource is None:
        return jsonify({'error': 'Resource not found'}), 404

    return jsonify(updated_resource)

@app.route('/api/v1/resource/<int:id>', methods=['DELETE'])
def delete_resource(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM resources WHERE id = %s RETURNING id', (id,))
    deleted_id = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if deleted_id is None:
        return jsonify({'error': 'Resource not found'}), 404

    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


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
