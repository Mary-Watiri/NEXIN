from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
import os
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///users.db')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'default_secret_key')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class Staff(db.Model):
    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255), unique=True, nullable=False)
    user_email = db.Column(db.String(255), unique=True, nullable=False)
    position = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Staff {self.user_name}>'

@app.route('/signup', methods=['POST'])
def signup():
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)
    user_name = request.json.get('user_name', None)
    user_email = request.json.get('user_email', None)
    position = request.json.get('position', None)
    password = request.json.get('password', None)

    if not all([first_name, last_name, user_name, user_email, position, password]):
        return jsonify({"msg": "Missing information"}), 400

    if Staff.query.filter_by(user_name=user_name).first() is not None:
        return jsonify({"msg": "Username already taken"}), 409

    if Staff.query.filter_by(user_email=user_email).first() is not None:
        return jsonify({"msg": "Email already registered"}), 409

    new_staff = Staff(
        first_name=first_name,
        last_name=last_name,
        user_name=user_name,
        user_email=user_email,
        position=position
    )
    new_staff.set_password(password)
    db.session.add(new_staff)
    db.session.commit()

    return jsonify({"msg": "Staff member created"}), 201

@app.route('/login', methods=['POST'])
def login():
    user_name = request.json.get('user_name', None)
    password = request.json.get('password', None)

    staff_member = Staff.query.filter_by(user_name=user_name).first()
    if staff_member and staff_member.check_password(password):
        access_token = create_access_token(identity=user_name)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid username or password"}), 401

if __name__ == '__main__':
    db.create_all()
    port = int(os.environ.get('PORT', 5555))
    app.run(port=port, debug=True)
