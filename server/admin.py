from databaseconfig import db

class Admin(db.Model):
    __tablename__ = 'admin'
    
    staff_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    position = db.Column(db.Integer)
    phone_number = db.Column(db.String)
    email = db.Column(db.String(120), unique=True, nullable=False)
       
    tasks = db.relationship("Task", back_populates="admin")
    clients = db.relationship("Client", back_populates="admin")  # Note the plural form
    tickets = db.relationship("Ticket", back_populates="assign_to")
    
    
    def __repr__(self):
            return f"Admin('{self.first_name}', '{self.last_name}', '{self.user_name}', '{self.position}', '{self.phone_number}', '{self.email}')"