from databaseconfig import db
from client import Client
from admin import Admin
from tasks import Task
from tickets import Ticket
from app import app
from datetime import datetime

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

# # Use the app's context for database operations
    with app.app_context():
#     # Create the database tables
     db.create_all()
    
#     # Create admins
#     admin1 = Admin(username='johndoe', first_name='John', last_name='Doe', position='Manager', user_email='johndoe@example.com', phone_number='123-456-7890')
#     admin2 = Admin(username='alicep', first_name='Alice', last_name='Parker', position='Admin', user_email='alice@example.com', phone_number='987-654-3210')
#     admin3 = Admin(username='bobj', first_name='Bob', last_name='Jack', position='Staff', user_email='bob@example.com', phone_number='555-555-5555')
#     admin4 = Admin(username='emmat', first_name='Emma', last_name='Tailor', position='Staff', user_email='emma@example.com', phone_number='111-222-3333')
#     admin5 = Admin(username='davidli', first_name='David', last_name='Livingstone', position='Manager', user_email='david@example.com', phone_number='444-444-4444')


#     # Create clients
#     client1 = Client(id=1, user_name='JohnDoe', user_email='john@example.com', phone_number='123-456-7890')
#     client2 = Client(id=2, user_name='AliceSmith', user_email='alice@example.com', phone_number='987-654-3210')
#     client3 = Client(id=3, user_name='BobJohnson', user_email='bob@example.com', phone_number='555-555-5555')
#     client4 = Client(id=4, user_name='EmmaBrown', user_email='emma@example.com', phone_number='111-222-3333')
#     client5 = Client(id=5, user_name='DavidLee', user_email='david@example.com', phone_number='444-444-4444')

#     # Create tasks
#     task1 = Task(id=1, title='Complete Report', description='Write a detailed report summarizing the project progress.', status='In Progress', priority='High', assign_to=1)
#     task2 = Task(id=2, title='Fix Bug', description='Investigate and fix the issue reported by the client.', status='Open', priority='Medium', assign_to=2)
#     task3 = Task(id=3, title='Implement Feature', description='Implement the new feature according to the specifications provided.', status='Open', priority='High', assign_to=3)
#     task4 = Task(id=4, title='Test Application', description='Conduct thorough testing to ensure the application functions correctly.', status='Completed', priority='Low', assign_to=4)
#     task5 = Task(id=5, title='Optimize Code', description='Optimize the codebase to improve performance and efficiency.', status='In Progress', priority='Medium', assign_to=5)
    
#     #Create tickets
#     ticket1 = Ticket(id=1, status='Open', priority='High', deadline='2024-04-20 12:00:00', assign_to=1, client_id=1)
#     ticket2 = Ticket(id=2, status='Closed', priority='Low', deadline='2024-04-22 10:30:00', assign_to=2, client_id=2)
#     ticket3 = Ticket(id=3, status='In Progress', priority='Medium', deadline='2024-04-25 15:45:00', assign_to=3, client_id=3)
#     ticket4 = Ticket(id=4, status='Open', priority='High', deadline='2024-04-28 09:00:00', assign_to=4, client_id=4)
#     ticket5 = Ticket(id=5, status='Open', priority='Low', deadline='2024-04-30 14:00:00', assign_to=5, client_id=5)

#     # Add admin, clients, tasks and tickets to the session
#     db.session.add_all([admin1, admin2, admin3, admin4, admin5])

#     # Commit the session to the database
#     db.session.commit()
