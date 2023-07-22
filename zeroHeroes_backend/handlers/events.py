from sqlalchemy import create_engine, Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from flask import request, jsonify

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String(50), primary_key=True)

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    image_file_name = Column(String(200))
    title = Column(String(100))
    description = Column(Text)
    content = Column(Text)

    # Use secondary association table for many-to-many relationship
    users = relationship('User', secondary='user_events')

class UserEvent(Base):
    __tablename__ = 'user_events'

    user_id = Column(String(50), ForeignKey('users.id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)

engine = create_engine('mysql+mysqlconnector://root:password123@localhost/zero_heroes')
Session = sessionmaker(bind=engine)

# Create the user_interests and users tables
Base.metadata.create_all(engine)

def join_event(eventid, userid):
    session = Session()

    # Create new UserEvent instance and add it to the session
    user_event = UserEvent(user_id=userid, event_id=eventid)
    session.add(user_event)

    session.commit()

def get_events():
    session = Session()

    events = session.query(Event).all()
    events_data = [
        {
            'EventId': event.id,
            'Image File Name': event.image_file_name,
            'title': event.title,
            'Description': event.description,
            'Content': event.content,
            'UserIdList': [user.id for user in event.users]
        } 
        for event in events
    ]

    return events_data

def create_event(userid, image_file_name, title, description, content):
    # Start a new session
    session = Session()

    try:

        # Check if user exists
        user = session.query(User).filter(User.id == userid).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Create a new Event instance
        new_event = Event(image_file_name=image_file_name, title=title, description=description, content=content)

        # Add the user to the event's users
        new_event.users.append(user)

        # Add the new Event to the session
        session.add(new_event)

        # Commit the session to save the Event to the database
        session.commit()

        return jsonify({'message': 'Event created successfully.'}), 201

    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': 'Failed to create the event.', 'details': str(e)}), 500

    finally:
        session.close()
