from databaseconfig import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.staff_id'))
    admin = db.relationship("Admin", back_populates="clients")
    
    tickets = db.relationship("Ticket", back_populates="client")    