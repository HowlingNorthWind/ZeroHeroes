import pandas as pd
from sklearn.preprocessing import LabelEncoder

from surprise import Dataset, Reader
from surprise import KNNBasic
from surprise.model_selection import cross_validate

from collections import defaultdict

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Weightage for each item
weightage_dict = {
    'item1': 0.5,
    'item2': 0.7,
    'item3': 1.0,
    'item4': 0.3,
    'item5': 0.9,
}


def get_top_n(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

def get_data_for_recommendation():
        # User ID, Item ID, Rating, City
    data = [
        ['user1', 'item1', 4.0, 'Redlands'],
        ['user1', 'item2', 3.0, 'Redlands'],
        ['user1', 'item3', 5.0, 'Redlands'],
        ['user2', 'item1', 3.0, 'Los Angeles'],
        ['user2', 'item4', 2.0, 'Los Angeles'],
        ['user2', 'item5', 4.0, 'Los Angeles'],
        ['user3', 'item2', 3.0, 'Chicago'],
        ['user3', 'item3', 3.0, 'Chicago'],
        ['user3', 'item4', 4.0, 'Chicago'],
    ]
    return data


def recommend_knn(user_id):

    data = get_data_for_recommendation()

    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['user', 'item', 'rating', 'city'])

    # Encode 'city' as categorical feature
    encoder = LabelEncoder()
    df['city'] = encoder.fit_transform(df['city'])

    # Apply weightage to rating
    df['rating'] = df.apply(lambda row: row['rating'] * weightage_dict[row['item']], axis=1)

    # Define a reader with the scale/limit of the ratings
    min_rating = df['rating'].min()
    max_rating = df['rating'].max()
    reader = Reader(rating_scale=(min_rating, max_rating))

    # Load data from data frame
    data = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)

    # Use KNNBasic model for user-user collaborative filtering
    sim_options = {
        'name': 'cosine',
        'user_based': True  # compute  similarities between users
    }
    model = KNNBasic(sim_options=sim_options)

    # Train the model on the entire dataset
    trainset = data.build_full_trainset()
    model.fit(trainset)

    # Predict ratings for all pairs (u, i) that are NOT in the training set.
    testset = trainset.build_anti_testset()
    predictions = model.test(testset)

    top_n = get_top_n(predictions, n=10)

    # Return the recommended items for the input user
    return [iid for (iid, _) in top_n[user_id]]


def recommend_dl(user_id):

    data = get_data_for_recommendation()

    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['user', 'item', 'rating', 'city'])

    # Encode 'city' as categorical feature
    encoder = LabelEncoder()
    df['city'] = encoder.fit_transform(df['city'])

    # Apply weightage to rating
    df['rating'] = df.apply(lambda row: row['rating'] * weightage_dict[row['item']], axis=1)

    # Encode the categorical data
    user_encoder = LabelEncoder()
    item_encoder = LabelEncoder()

    df['user'] = user_encoder.fit_transform(df['user'])
    df['item'] = item_encoder.fit_transform(df['item'])

    # Split the data into training and test sets
    train, test = train_test_split(df, test_size=0.2)

        # Create user-item matrix
    num_users = df['user'].nunique()
    num_items = df['item'].nunique()

    user_item_matrix = np.zeros((num_users, num_items))
    for row in train.itertuples():
        user_item_matrix[row[1], row[2]] = row[3]

    # Define the Matrix Factorization model
    embedding_dim = 8
    user_input = tf.keras.Input(shape=(1,))
    item_input = tf.keras.Input(shape=(1,))

    user_embedding = tf.keras.layers.Embedding(num_users, embedding_dim)(user_input)
    item_embedding = tf.keras.layers.Embedding(num_items, embedding_dim)(item_input)

    dot_product = tf.keras.layers.Dot(axes=2)([user_embedding, item_embedding])
    flatten_output = tf.keras.layers.Flatten()(dot_product)

    model = tf.keras.Model(inputs=[user_input, item_input], outputs=flatten_output)

    # Compile the model
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Train the model
    train_user_input = train['user'].values
    train_item_input = train['item'].values
    train_target = train['rating'].values

    model.fit([train_user_input, train_item_input], train_target, epochs=100, batch_size=32, verbose=1)

    # Make predictions on the test set
    test_user_input = test['user'].values
    test_item_input = test['item'].values

    predictions = model.predict([test_user_input, test_item_input])

    # Get the indices of items sorted by predicted rating for each user
    sorted_item_indices = np.argsort(-predictions)

    # Number of top items to recommend
    top_n = 5

    # Create a dictionary to store recommended items for each user
    recommendations = {}

    for i, user_id in enumerate(test['user'].unique()):
        # Get the top N item indices for the current user
        top_indices = sorted_item_indices[i][:top_n]
        
        # Convert item indices back to original item IDs
        top_items = item_encoder.inverse_transform(top_indices)
        
        # Add the recommended items to the dictionary
        recommendations[user_id] = list(top_items)


    # Return the recommended items for the input user
    return [iid for iid in recommendations[user_id]]

