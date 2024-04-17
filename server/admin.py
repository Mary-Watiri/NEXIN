from databaseconfig import db
from sqlalchemy.orm import validates

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
    
    @validates('first_name', 'last_name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name is required")
        if len(name) >= 50:
            raise ValueError("Name must be less than 50")
        
        return name
    
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if phone_number and not all(c.isdigit() or c in '- ()' for c in phone_number):
            raise ValueError("Phone number must contain only digits and standard separators (dashes, spaces).")
        if len(phone_number) >= 10:
            raise ValueError("Phone number must be less than 15")
        
        return phone_number
    
    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Wrong email format")
        
        return email
    
    def __repr__(self):
            return f"Admin('{self.first_name}', '{self.last_name}', '{self.user_name}', '{self.position}', '{self.phone_number}', '{self.email}')"