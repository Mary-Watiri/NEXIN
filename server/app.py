from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from databaseconfig import db
from endpoints.client_api import clients
from endpoints.tickets_api import tickets
from endpoints.admin_api import admin


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h3>Nexin LTD</h3>'

app.add_url_rule('/admin', 'admin', admin, methods=['GET', 'POST'])
app.add_url_rule('/clients', 'clients', clients, methods=['GET', 'POST'])
app.add_url_rule('/tickets', 'tickets', tickets, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(port=5555, debug=True)