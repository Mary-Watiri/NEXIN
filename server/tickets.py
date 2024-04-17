from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    deadline = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    assign_to = db.Column(db.Integer, db.ForeignKey('staff.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
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

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
