
# app/routes.py

from flask import jsonify, request
from app import app

from handlers.user_interests import set_interests

from handlers.events import get_events, join_event, create_event

from handlers.rating import give_rating

from handlers.recommend import recommend_knn, recommend_dl
# Define your API endpoints and route handlers here.
@app.route('/api/data', methods=['GET'])
def get_data_route():
    return get_data()

@app.route('/api/get_recommendation_dl/<user_id>', methods=['GET'])
def get_recommendation_dl_route(user_id):
    recommendations = recommend_dl(user_id)
    # Convert the NumPy int64 data to Python integers using .tolist()
    recommendations = [int(item) for item in recommendations]
    return jsonify({'recommendations': recommendations})

@app.route('/api/get_recommendation_knn/<user_id>', methods=['GET'])
def get_recommendation_knn_route(user_id):
    recommendations = recommend_knn(user_id)
    # Convert the NumPy int64 data to Python integers using .tolist()
    recommendations = [int(item) for item in recommendations]
    return jsonify({'recommendations': recommendations})
    # return recommend_dl(user_id)

app.route('/api/set_interests', methods=['POST'])(set_interests)  # Register the function as a route

app.route('/api/give_rating', methods=['POST'])(give_rating)  # Register the function as a route

# app.route('/api/init_recommendation_data', methods=['POST'])(init_recommendation_data)  # Register the function as a route

@app.route('/api/get_events', methods=['GET'])
def events_route():
    events = get_events()  # Call the function to get the events
    return jsonify({'eventsList': events})

@app.route('/api/join_event', methods=['POST'])
def join_event_route():
    data = request.get_json()  # Get the posted data

    # Check if 'eventid' and 'userid' are in the posted data
    if 'EventId' not in data or 'UserId' not in data:
        return jsonify({'error': 'eventid or userid missing from request'}), 400

    eventid = data['EventId']
    userid = data['UserId']

    join_event(eventid, userid)  # Call the function to join the event

    return jsonify({'status': 'success'}), 200

@app.route('/api/create_event', methods=['POST'])
def create_event_route():
    data = request.get_json()  # Get the posted data

    # Check if all required parameters are in the posted data
    required_params = ['UserId', 'ImageFileName', 'title', 'Description', 'Content']
    if not all(param in data for param in required_params):
        return jsonify({'error': 'Required parameter(s) missing from request'}), 400

    userid = data['UserId']
    image_file_name = data['ImageFileName']
    title = data['title']
    description = data['Description']
    content = data['Content']

    create_event(userid, image_file_name, title, description, content)  # Call the function to create the event

    return jsonify({'status': 'success'}), 200

# You can remove this route handler since it will be handled by login_handler.
# @app.route('/api/login', methods=['POST'])
# def login():
#     return login()

# You can remove this route handler since it will be handled by activity_handler.
# @app.route('/api/user/activities', methods=['POST'])
# def submit_activity():
#     return submit_activity()

# Define other endpoints and handlers similarly.
