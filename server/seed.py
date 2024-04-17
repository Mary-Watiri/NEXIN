from databaseconfig import db
from client import Client
from admin import Admin
from tasks import Task
from tickets import Ticket
from app import app


# Use the app's context for database operations
with app.app_context():
    # Create the database tables
    db.create_all()
    
    # Create admins
    Admin1 = Admin(username='johndoe', first_name='John', last_name='Doe', position='Manager', user_email='johndoe@example.com', phone_number='123-456-7890')
    Admin2 = Admin(username='alicep', first_name='Alice', last_name='Parker', position='Admin', user_email='alice@example.com', phone_number='987-654-3210')
    Admin3 = Admin(username='bobj', first_name='Bob', last_name='Jack', position='Staff', user_email='bob@example.com', phone_number='555-555-5555')
    Admin4 = Admin(username='emmat', first_name='Emma', last_name='Tailor', position='Staff', user_email='emma@example.com', phone_number='111-222-3333')
    Admin5 = Admin(username='davidli', first_name='David', last_name='Livingstone', position='Manager', user_email='david@example.com', phone_number='444-444-4444')


    # Create clients
    Client1 = Client(id=1, user_name='JohnDoe', user_email='john@example.com', phone_number='123-456-7890')
    Client2 = Client(id=2, user_name='AliceSmith', user_email='alice@example.com', phone_number='987-654-3210')
    Client3 = Client(id=3, user_name='BobJohnson', user_email='bob@example.com', phone_number='555-555-5555')
    Client4 = Client(id=4, user_name='EmmaBrown', user_email='emma@example.com', phone_number='111-222-3333')
    Client5 = Client(id=5, user_name='DavidLee', user_email='david@example.com', phone_number='444-444-4444')

    # Create tasks
    Task1 = Task(id=1, title='Complete Report', description='Write a detailed report summarizing the project progress.', status='In Progress', priority='High', assign_to=1)
    Task2 = Task(id=2, title='Fix Bug', description='Investigate and fix the issue reported by the client.', status='Open', priority='Medium', assign_to=2)
    Task3 = Task(id=3, title='Implement Feature', description='Implement the new feature according to the specifications provided.', status='Open', priority='High', assign_to=3)
    Task4 = Task(id=4, title='Test Application', description='Conduct thorough testing to ensure the application functions correctly.', status='Completed', priority='Low', assign_to=4)
    Task5 = Task(id=5, title='Optimize Code', description='Optimize the codebase to improve performance and efficiency.', status='In Progress', priority='Medium', assign_to=5)
    
    #Create tickets
    Ticket1 = Ticket(id=1, status='Open', priority='High', deadline='2024-04-20 12:00:00', assign_to=1, client_id=1)
    Ticket2 = Ticket(id=2, status='Closed', priority='Low', deadline='2024-04-22 10:30:00', assign_to=2, client_id=2)
    Ticket3 = Ticket(id=3, status='In Progress', priority='Medium', deadline='2024-04-25 15:45:00', assign_to=3, client_id=3)
    Ticket4 = Ticket(id=4, status='Open', priority='High', deadline='2024-04-28 09:00:00', assign_to=4, client_id=4)
    Ticket5 = Ticket(id=5, status='Open', priority='Low', deadline='2024-04-30 14:00:00', assign_to=5, client_id=5)

    # Add admin, clients, tasks and tickets to the session
    db.session.add_all([Admin1, Admin2, Admin3, Admin4, Admin5])

    # Commit the session to the database
    db.session.commit()
