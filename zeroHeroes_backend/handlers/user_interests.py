# user_interests.py

from flask import request, jsonify
from sqlalchemy import create_engine, Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String(50), primary_key=True)

class UserInterest(Base):
    __tablename__ = 'user_interests'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), ForeignKey('users.id'))
    interest = Column(String(50)) 

# Set up SQLAlchemy engine and session
engine = create_engine('mysql+mysqlconnector://root:password123@localhost/zero_heroes')
Session = sessionmaker(bind=engine)

def set_interests():
    data = request.get_json()  # Get the POSTed JSON data

    if 'UserId' not in data or 'interests' not in data:
        return jsonify({'error': 'user_id or interests missing from request'}), 400

    userid = data['UserId']
    interests = data['interests']

    if not isinstance(interests, list):
        return jsonify({'error': 'interests must be a list'}), 400

    # Create the user_interests and users tables
    Base.metadata.create_all(engine)

    # Start a new session
    session = Session()

    # Create the user if they don't exist
    user = session.query(User).filter(User.id == userid).first()
    if not user:
        user = User(id=userid)
        session.add(user)

    # Create a new UserInterest for each interest and add it to the session
    for interest in interests:
        new_interest = UserInterest(user_id=userid, interest=interest)
        session.add(new_interest)

    # Commit the session
    session.commit()

    return jsonify({'status': 'success'}), 200
