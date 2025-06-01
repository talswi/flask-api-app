from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient


mongo_client = MongoClient("mongodb://mongo:27017/")
db = mongo_client["mydb"]
users_collection = db["users"]

print("Loading users_routes blueprint...")

# Blueprint
users_routes = Blueprint('users', __name__)

# Register
@users_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if users_collection.find_one({"username": username}):
        return jsonify({"error": "User already exists"}), 400
    
    hashed_password = generate_password_hash(password)
    users_collection.insert_one({
        "username": username,
        "password": hashed_password
    })
    
    return jsonify({"status": "user created"})

# Login
@users_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    user = users_collection.find_one({"username": username})
    if user and check_password_hash(user['password'], password):
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"}), 401

