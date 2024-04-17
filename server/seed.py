from databaseconfig import db
from client import Client
from tasks import Task
from app import app


# Use the app's context for database operations
with app.app_context():
    # Create the database tables
    db.create_all()

    # Create clients
    client1 = Client(username='Mary Watiri', email='mary@example.com')
    client2 = Client(username='Samuel Omoding', email='sam@example.com')

    # Create tasks
    task1 = Task(title='Task 1', description='Description for Task 1')
    task2 = Task(title='Task 2', description='Description for Task 2')

    # Add clients and tasks to the session
    db.session.add_all([client1, client2, task1, task2])
    

    # Commit the session to the database
    db.session.commit()
from models import User  # Import your User model (assuming it's defined in models.py)

def seed_database():
    # Create some sample users
    users = [
        User(username='user1', email='user1@example.com', password='password1'),
        User(username='user2', email='user2@example.com', password='password2'),
        # Add more users as needed
    ]

    # Add users to the session
    for user in users:
        db.session.add(user)

    # Commit the session to the database
    db.session.commit()