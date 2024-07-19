from flask import Flask, jsonify, request, current_app
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['sindhu']  # Ensure we are using the 'sindhu' database

# JWT Secret Key
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)  # Token expiration period

# Make the database accessible to routes
app.config['db'] = db

# Register endpoint
@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    try:
        # Check if user already exists
        existing_user = db.users.find_one({'email': email})
        if existing_user:
            return jsonify({'message': 'Email already registered'}), 400

        # Insert new user
        user_id = db.users.insert_one({
            'username': username,
            'email': email,
            'password': hashed_password
        }).inserted_id

        return jsonify({'message': 'Registration successful', 'user_id': str(user_id)}), 201
    except Exception as e:
        return jsonify({'message': f'Registration failed: {str(e)}'}), 500

# Login endpoint
@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user = db.users.find_one({'email': email})
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Create JWT token
    token = jwt.encode({'id': str(user['_id']), 'exp': datetime.utcnow() + app.config['JWT_EXPIRATION_DELTA']}, app.config['JWT_SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token.decode('UTF-8')}), 200

# Example route to verify authentication (protected route)
@app.route('/api/notes', methods=['GET'])
def get_notes():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Missing token'}), 401

    try:
        decoded_token = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        user_id = decoded_token['id']
        notes = list(db.notes.find({'user_id': user_id}))
        return jsonify({'notes': notes}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

# Other routes and configurations...

if __name__ == '__main__':
    app.run(port=5000, debug=True)
