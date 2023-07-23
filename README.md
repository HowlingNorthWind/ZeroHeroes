# ZeroHeroes

ZeroHeroes is a mobile application with the mission of promoting waste-free living. The app provides activity recommendations and event management features to encourage users to adopt eco-friendly habits and participate in waste reduction initiatives.

## Features

- Activity Recommendations: ZeroHeroes suggests a variety of waste-free activities based on user interests and preferences. Users can explore sustainable lifestyle choices and discover new ways to reduce waste in their daily lives.

- Event Management: The app allows users to create and join waste-free events within their communities. Whether it's a zero-waste workshop, clean-up campaign, or sustainable market, users can connect with like-minded individuals to make a positive impact together.

## Recommendation Algorithms

ZeroHeroes utilizes two different recommendation algorithms to provide users with personalized waste-free activity suggestions:

### K-Nearest Neighbors (KNN)

**Strengths:**  

- Collaborative Filtering: KNN is a collaborative filtering algorithm, which means it relies on user-item interactions to make recommendations.
- No Training Phase: KNN is a lazy learning algorithm, meaning it does not require a separate training phase. Recommendations are made based on similarity calculations at runtime.

**Use Cases:**

- KNN is suitable for small to medium-sized recommendation systems with dense user-item interaction data.
- It works well when there is sufficient user data available for making accurate similarity calculations.
- KNN is effective for providing personalized recommendations based on user preferences and item similarities.

### Matrix Factorization

**Strengths:**

- Personalization: Matrix factorization can capture latent features and preferences of users and items, leading to highly personalized recommendations.
- Scalability: With the use of matrix decomposition techniques, matrix factorization can handle large-scale data efficiently.
- Handling Sparsity: Matrix factorization can handle sparse data better than KNN, making it suitable for situations with limited user-item interactions.

**Use Cases:**

- Matrix factorization is ideal for large-scale recommendation systems with sparse data, such as e-commerce and streaming platforms.
- It excels at providing accurate and personalized recommendations based on learned user and item features.
- Matrix factorization is well-suited for situations where there is a need for handling scalability and sparsity in the recommendation data.

In summary, ZeroHeroes uses both K-Nearest Neighbors (KNN) and Matrix Factorization to provide users with diverse and personalized waste-free activity recommendations. KNN is simple and effective for smaller recommendation systems with dense data, while Matrix Factorization excels in handling large-scale and sparse data, offering highly personalized suggestions. The choice between the two algorithms depends on the specific requirements and characteristics of the recommendation application.

## Join the ZeroHeroes Movement

Download ZeroHeroes now and become part of a growing community committed to living waste-free and creating a cleaner, healthier planet for future generations. Together, we can make a significant difference and leave a positive impact on the world. Let's embark on this journey toward a more sustainable future!

## API Documentation

For detailed API documentation, please refer to [API Documentation](https://docs.google.com/spreadsheets/d/18cMsfAd452XRPyuLJUjm_Iuk32PIuMxp91Tw0rNlvd4/edit#gid=0).

## Description

The mobile application allows users to receive personalized activity recommendations based on their interests and previous activity ratings. Users can also create, join, and manage events within the platform. The system utilizes collaborative filtering and deep learning algorithms to provide accurate recommendations.

## Setup and Installation

0. Set up your MySQL: username: `root` password: `password123` dbname:`zero_heroes`
1. Clone the repository: `git clone https://github.com/HowlingNorthWind/ZeroHeroes.git`
2. Create a new conda environment: `conda create --name ZeroHeroes`
3. Switch to the new conda environment: `conda activate ZeroHeroes`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Enter the backend folder:  `cd zeroHeroes_backend`
6. Run the application: `python run.py`
7. Access the web application through the browser at `http://localhost:5000`
