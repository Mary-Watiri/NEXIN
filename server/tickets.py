from databaseconfig import db

class Ticket(db.Model):
    __tablename__ = 'ticket'
    
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum('Open', 'Closed', 'In Progress'), nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    assign_to_id = db.Column(db.Integer, db.ForeignKey('admin.staff_id'))  
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))  
    
    assign_to = db.relationship("Admin", back_populates="tickets", foreign_keys=[assign_to_id])    
    client = db.relationship("Client", back_populates="tickets")
    
    def __repr__(self):
        return f"Ticket(id={self.id}, status='{self.status}', priority='{self.priority}', deadline='{self.deadline}', assign_to_id='{self.assign_to_id}', client_id='{self.client_id}')"
