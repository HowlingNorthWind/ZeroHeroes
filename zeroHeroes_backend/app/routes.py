
# app/routes.py

from flask import jsonify
from app import app
from handlers.get_users import get_data
from handlers.recommend import recommend_dl, recommend_knn

# Define your API endpoints and route handlers here.
@app.route('/api/data', methods=['GET'])
def get_data_route():
    return get_data()

@app.route('/api/recommend_dl/<user_id>', methods=['GET'])
def recommend_dl_route(user_id):
    return recommend_dl(user_id)

@app.route('/api/recommend_knn/<user_id>', methods=['GET'])
def recommend_knn_route(user_id):
    return recommend_knn(user_id)

# You can remove this route handler since it will be handled by login_handler.
# @app.route('/api/login', methods=['POST'])
# def login():
#     return login()

# You can remove this route handler since it will be handled by activity_handler.
# @app.route('/api/user/activities', methods=['POST'])
# def submit_activity():
#     return submit_activity()

# Define other endpoints and handlers similarly.
