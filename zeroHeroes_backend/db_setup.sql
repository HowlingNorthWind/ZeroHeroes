create database zero_heroes;
use zero_heroes;

CREATE TABLE users (
  user_id INT PRIMARY KEY,
  username VARCHAR(255) UNIQUE,
  password VARCHAR(255),
  name VARCHAR(255)
);


CREATE TABLE activities (
  activity_id INT PRIMARY KEY,
  activity_type VARCHAR(255),
  weightage INT
);


CREATE TABLE user_activities (
  user_activity_id INT PRIMARY KEY,
  user_id INT,
  activity_id INT,
  quantity INT,
  timestamp TIMESTAMP,
  rating INT,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (activity_id) REFERENCES activities(activity_id)
);

CREATE TABLE teams (
  team_id INT PRIMARY KEY,
  team_name VARCHAR(255),
  location_polygon GEOMETRY
);

CREATE TABLE user_teams (
  user_team_id INT PRIMARY KEY,
  user_id INT,
  team_id INT,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE badges (
  badge_id INT PRIMARY KEY,
  badge_name VARCHAR(255),
  threshold INT
);

CREATE TABLE user_badges (
  user_badge_id INT PRIMARY KEY,
  user_id INT,
  badge_id INT,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (badge_id) REFERENCES badges(badge_id)
);
