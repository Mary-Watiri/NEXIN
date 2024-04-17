# from flask import Flask, jsonify, make_response
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from sqlalchemy import MetaData
# from databaseconfig import db


# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.json.compact = False

# migrate = Migrate(app, db)

# db.init_app(app)

# @app.route('/')
# def index():
#     return '<h3>Nexin LTD</h3>'

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os
from dotenv import load_dotenv
load_dotenv()  


# Separate file for users database (e.g., users_db.py)
from users_db import users

app = Flask(__name__)

# It's a good practice to keep your secret keys in environment variables
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'default_secret_key')
jwt = JWTManager(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the home page!'})

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = users.get(username)
    if not user or user['password'] != password:
        return jsonify({"msg": "Invalid username or password"}), 401

    # Create a new access token
    access_token = create_access_token(identity={'username': username, 'role': user['role']})
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    # Use an environment variable for the port as well
    port = int(os.environ.get('PORT', 5555))
    app.run(port=port, debug=True)
