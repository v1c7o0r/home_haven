from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Room, Booking, Review  # Assuming your models are defined here

engine = create_engine('your_database_uri')
Session = sessionmaker(bind=engine)
session = Session()

users = [
    User(name='James Bond', email='jamesbond@gmail.com', password='James5566'),
    User(name='Jane Quartz', email='jquartz13@gmail.com', password='jQuarTz13'),
]

rooms = [
    Room(number='420', type='single', price=10000, availability=True),
    Room(number='690', type='double', price=15000, availability=True),
]

bookings = [
    Booking(user=users[0], room=rooms[0], check_in='2024-11-01', check_out='2024-11-05'),
    Booking(user=users[1], room=rooms[1], check_in='2024-11-10', check_out='2024-11-15'),
]

reviews = [
    Review(user=users[0], room=rooms[0], rating=5, comment='The room was quite luxurious and comfortable.'),
    Review(user=users[1], room=rooms[1], rating=4, comment='Moderate stay could have been way better.'),
    Review(user=users[0], room=rooms[1], rating=3, comment='Some of the facilities were not working'),
    Review(user=users[1], room=rooms[0], rating=4, comment='The food was quite good and the beds were comfortable')
]

session.add_all(users)
session.add_all(rooms)
session.add_all(bookings)
session.add_all(reviews)
session.commit()
