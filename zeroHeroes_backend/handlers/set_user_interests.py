# user_interests.py

from flask import request, jsonify
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserInterest(Base):
    __tablename__ = 'user_interests'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    interest = Column(String(50))

# Set up SQLAlchemy engine and session
engine = create_engine('mysql+mysqlconnector://root:password123@localhost/zero_heroes')
Session = sessionmaker(bind=engine)

def set_interests():
    data = request.get_json()  # Get the POSTed JSON data

    if 'userid' not in data or 'interests' not in data:
        return jsonify({'error': 'user_id or interests missing from request'}), 400

    userid = data['UserId']
    interests = data['interests']

    if not isinstance(interests, list):
        return jsonify({'error': 'interests must be a list'}), 400

    # TODO: Add code here to save the interests for the user in the database
    # Create the user_interests table
    Base.metadata.create_all(engine)

    # Start a new session
    session = Session()

    # Create a new UserInterest for each interest and add it to the session
    for interest in interests:
        new_interest = UserInterest(user_id=userid, interest=interest)
        session.add(new_interest)

    # Commit the session
    session.commit()

    return jsonify({'status': 'success'}), 200
