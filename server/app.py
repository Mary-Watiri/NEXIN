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
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from enum import Enum

# Create Flask app
app = Flask(__name__)

# Configure SQLAlchemy to use SQLite and store the database file as app.db in the root directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

class TicketStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    IN_PROGRESS = "in_progress"
    
class PriorityLevel(Enum):
    URGENT = "urgent"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
   
class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(TicketStatus), default=TicketStatus.OPEN)
    priority = db.Column(db.Enum(PriorityLevel), default=PriorityLevel.LOW)
    deadline = db.Column(db.DateTime, nullable=False)
    assign_to = db.Column(db.Integer, db.ForeignKey('staff.id'))  
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))  
    tasks = db.relationship('Task', back_populates='ticket')  

    @property
    def days_remaining(self):
        return (self.deadline - datetime.utcnow()).days

    @property
    def is_urgent(self):
        return self.days_remaining < 3 

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'))
    ticket = db.relationship('Ticket', back_populates='tasks')  

class Staff(db.Model):
    __tablename__ = 'staff'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
