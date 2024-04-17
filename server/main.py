#!/usr/bin/env python3
# from dotenv import load_dotenv

from config import db
from flask import Flask, jsonify, render_template, request
from flask_migrate import Migrate
from server.app.clients.models import Client
from server.app.staff.models import Staff
from server.app.tasks.models import Tasks
# from flask_restful import Api, Resource

# Load environment variables from .env file
# load_dotenv


app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False


# Initialize the Flask app with the SQLAlchemy instance
db.init_app(app)
# Create the migration instance
migrate = Migrate(app, db)


@app.route('/')
def home():
    return '<h3>Nexin Project</h3>'
    # return app.send_static_file('index.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('index.html')

@app.route('/admin')
def admin():
    pass
@app.route('/client')
def client():
    pass
@app.route('/tasks')
def tasks():
    pass
@app.route('/tickets')
def tickets():
    pass


if __name__ == '__main__':
    app.run(port=5000, debug=True)
