from databaseconfig import db
from client import Client
from admin import Admin
from tasks import Task
from tickets import Ticket
from app import app
from datetime import datetime

with app.app_context():

    def seed_data():
        # Clear existing data
        db.session.query(Admin).delete()
        db.session.query(Client).delete()
        db.session.query(Task).delete()
        db.session.query(Ticket).delete()

        # Create new entries
        # Admins
        admin1 = Admin(first_name='Sang', last_name='Wicklif', user_name='sangw', position=1, phone_number='1234567890', email='sang@example.com')
        admin2 = Admin(first_name='Mary', last_name='Watiri', user_name='mw', position=2, phone_number='2345678901', email='mary.w@example.com')

        # Clients
        client1 = Client(username='clientone', email='client1@example.com', admin=admin1)
        client2 = Client(username='clienttwo', email='client2@example.com', admin=admin2)

        # Tasks
        task1 = Task(title='Database Migration', description='Migrate the database to a new version.', admin_id=admin1.staff_id)
        task2 = Task(title='API Development', description='Develop the new version of API.', admin_id=admin2.staff_id)

        # Tickets
        ticket1 = Ticket(status='Open', priority='High', deadline=datetime(2024, 5, 1), assign_to=admin1, client=client1)
        ticket2 = Ticket(status='Closed', priority='Low', deadline=datetime(2024, 6, 1), assign_to=admin2, client=client2)

        # Add to session and commit
        db.session.add_all([admin1, admin2, client1, client2, task1, task2, ticket1, ticket2])
        db.session.commit()

    if __name__ == '__main__':
        seed_data()
        print("Database seeded successfully!")

    #     # Create the database tables
        db.create_all()
        

