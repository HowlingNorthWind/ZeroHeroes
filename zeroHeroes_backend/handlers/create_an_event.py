# event_actions.py

# event_actions.py

from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    image_file_name = Column(String(200))
    title = Column(String(100))
    description = Column(Text)
    content = Column(Text)

# Set up SQLAlchemy engine and session
engine = create_engine('mysql+mysqlconnector://root:password123@localhost/zero_heroes')
Session = sessionmaker(bind=engine)

def create_event(userid, image_file_name, title, description, content):
    # Create the events table if it doesn't exist
    Base.metadata.create_all(engine)

    # Start a new session
    session = Session()

    # Create a new Event instance
    new_event = Event(user_id=userid, image_file_name=image_file_name, title=title, description=description, content=content)

    # Add the new Event to the session
    session.add(new_event)

    # Commit the session to save the Event to the database
    session.commit()

    return



# def create_event(userid, image_file_name, title, description, content):
#     # TODO: Add code here to create the event in your data source (e.g., a database)
#     return
