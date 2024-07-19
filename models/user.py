# user.py

from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, email, password):
    db = current_app.config['db']
    users_collection = db['users']
    hashed_password = generate_password_hash(password, method='sha256')
    user = {
        "username": username,
        "email": email,
        "password": hashed_password
    }
    users_collection.insert_one(user)

def find_user_by_email(email):
    db = current_app.config['db']
    users_collection = db['users']
    return users_collection.find_one({"email": email})

def check_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)
