from sqlalchemy import create_engine, Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from flask import request, jsonify
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String(50), primary_key=True)

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), ForeignKey('users.id'))
    activity = Column(Integer)
    rating = Column(Integer)

# Configure the database engine
engine = create_engine('mysql+mysqlconnector://root:password123@localhost/zero_heroes')
Session = sessionmaker(bind=engine)

# Create the tables
Base.metadata.create_all(engine)

# Define the API endpoint to give a rating
def give_rating():
    data = request.get_json()

    # Check if all required parameters are present
    required_params = ['UserId', 'Activity', 'Rating']
    if not all(param in data for param in required_params):
        return jsonify({'error': 'Required parameter(s) missing from request'}), 400

    userid = data['UserId']
    activity = data['Activity']
    rating = data['Rating']

    # Check if the user exists
    session = Session()
    user = session.query(User).filter(User.id == userid).first()
    if not user:
        session.close()
        return jsonify({'error': 'User not found'}), 404

    try:
        # Check if the rating record already exists
        existing_rating = session.query(Rating).filter(Rating.user_id == userid, Rating.activity == activity).first()

        if not existing_rating:
            # Rating record does not exist, create a new one
            new_rating = Rating(user_id=userid, activity=activity, rating=rating)
            session.add(new_rating)
            session.commit()
            session.close()
            return jsonify({'message': 'Rating added successfully'}), 201
        else:
            # Rating record already exists, update the rating value
            existing_rating.rating = rating
            session.merge(existing_rating)
            session.commit()
            session.close()
            return jsonify({'message': 'Rating updated successfully'}), 200


    except SQLAlchemyError as e:
        session.rollback()
        session.close()
        return jsonify({'error': 'Failed to add rating', 'details': str(e)}), 500

def get_ratings_from_database():
    # Configure the database engine
    engine = create_engine('mysql+mysqlconnector://root:password123@localhost/zero_heroes')
    Session = sessionmaker(bind=engine)

    # Create the session
    session = Session()

    try:
        # Get all the ratings from the 'ratings' table
        ratings_data = session.query(Rating).all()

        # Create a list to store the ratings data
        ratings = []

        # Iterate through the ratings and append them to the list
        for rating_obj in ratings_data:
            rating_info = {
                'UserId': rating_obj.user_id,
                'Activity': rating_obj.activity,
                'Rating': rating_obj.rating
            }
            ratings.append(rating_info)

        return ratings

    except SQLAlchemyError as e:
        # Handle any errors that occur while querying the database
        print(f"Error retrieving ratings from the database: {e}")
        return []

    finally:
        # Close the session
        session.close()

def get_data_for_recommendation_from_database():
    # Get the ratings from the database
    ratings = get_ratings_from_database()

    # Prepare the data in the same format as the get_data_for_recommendation function
    data = []
    for rating in ratings:
        data.append([rating['UserId'], rating['Activity'], rating['Rating']])

    return data


def give_rating_with_args(user_id, activity, rating):
    session = Session()

    try:
        existing_rating = session.query(Rating).filter(Rating.user_id == user_id, Rating.activity == activity).first()

        if not existing_rating:
            new_rating = Rating(user_id=user_id, activity=activity, rating=rating)
            session.add(new_rating)
            session.commit()
            print(f"Rating for User '{user_id}', Activity '{activity}' with rating '{rating}' added successfully.")
        else:
            existing_rating.rating = rating
            session.merge(existing_rating)
            session.commit()
            print(f"Rating for User '{user_id}', Activity '{activity}' updated to rating '{rating}'.")

    except Exception as e:
        session.rollback()
        print(f"Failed to add rating for User '{user_id}', Activity '{activity}'. Error: {str(e)}")

    finally:
        session.close()

def register_users(data):
    session = Session()

    try:
        for user_data in data:
            user_id = user_data[0]

            existing_user = session.query(User).filter(User.id == user_id).first()

            if not existing_user:
                user = User(id=user_id)
                session.add(user)

        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        print(f"Failed to register users. Error: {str(e)}")

    finally:
        session.close()


def init_recommendation_data():
    data_2 = [
        ['user1', 1, 4.0],
        ['user1', 2, 3.0],
        ['user1', 3, 5.0],
        ['user2', 1, 3.0],
        ['user2', 4, 2.0],
        ['user2', 5, 4.0],
        ['user3', 2, 3.0],
        ['user3', 3, 3.0],
        ['user3', 4, 4.0],
    ]
    # First, let's register all the users
    user_ids = set(record[0] for record in data_2)
    users_data = [[user_id] for user_id in user_ids]
    register_users(users_data)

    for record in data_2:
        user_id, activity, rating = record
        give_rating_with_args(user_id, activity, rating)

init_recommendation_data()