# backend/routes/auth.py

from flask import Blueprint, request, jsonify, current_app
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_mail import Mail, Message
from backend.models.user import create_user, find_user_by_email, check_password  # Update the import path

auth = Blueprint('auth', __name__)

mail = Mail()

# Utility function to send reset email
def send_reset_email(user):
    token = generate_reset_token(user['email'])
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user['email']])
    msg.body = f'''To reset your password, visit the following link:
{request.host_url}api/auth/reset_password/{token}

If you did not make this request then simply ignore this email.
'''
    mail.send(msg)

# Utility function to generate a reset token
def generate_reset_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

# Utility function to verify a reset token
def verify_reset_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except SignatureExpired:
        return None
    return email

@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({"message": "All fields are required"}), 400

        existing_user = find_user_by_email(email)
        if existing_user:
            return jsonify({"message": "User already exists"}), 400

        create_user(username, email, password)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        user = find_user_by_email(email)
        if user and check_password(user['password'], password):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@auth.route('/reset_password_request', methods=['POST'])
def reset_request():
    try:
        data = request.get_json()
        email = data.get('email')

        user = find_user_by_email(email)
        if user:
            send_reset_email(user)
        return jsonify({"message": "If an account with that email exists, a reset link has been sent."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@auth.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
    try:
        data = request.get_json()
        password = data.get('password')

        email = verify_reset_token(token)
        if not email:
            return jsonify({"message": "Token is invalid or has expired"}), 401

        # Update password in the database
        # Replace this logic with your actual database update code
        # Example (assuming you have a user collection in MongoDB):
        # db.users.update_one({"email": email}, {"$set": {"password": password}})
        
        return jsonify({"message": "Password has been reset"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
