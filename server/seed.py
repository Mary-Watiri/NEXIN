from databaseconfig import db
from client import Client
from tasks import Task
from tickets import Ticket
from app import app
from tickets import TicketStatus
from tickets import PriorityLevel
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError

# Use the app's context for database operations
with app.app_context():
    # Create the database tables
    db.create_all()
      # Create contacts
    contact1 = Contact(name='John Kent', position='Manager', organization_id=1)  # Assuming organization with id 1
    contact2 = Contact(name='Janet ', position='Developer', organization_id=2)  
    # Create clients
    client1 = Client(username='Mary Watiri', email='mary@example.com')
    client2 = Client(username='Samuel Omoding', email='sam@example.com')

    # Create tasks
    task1 = Task(title='Task 1', description='Description for Task 1')
    task2 = Task(title='Task 2', description='Description for Task 2')

    # Create a new ticket instance
    new_ticket = Ticket(
        status=TicketStatus.OPEN,
        priority=PriorityLevel.HIGH,
        deadline=datetime.utcnow() + timedelta(days=7),  # Set deadline 7 days from now
        assign_to=1,  # Assuming staff with id 1
        client_id=1   # Assuming client with id 1
    )

    # Add clients, tasks, and the new ticket to the session
    db.session.add_all([client1, client2, task1, task2, new_ticket])

    # Try to commit the session to save the objects to the database
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()  # Roll back the transaction
        # Handle the error, e.g., by informing the user or logging the error
        print("The email address already exists in the database.")
