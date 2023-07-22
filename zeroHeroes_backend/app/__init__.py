# app/__init__.py

from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)


# MySQL configurations 
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password123'
app.config['MYSQL_DATABASE_DB'] = 'zero_heroes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# Initialize the MySQL connection
mysql = MySQL()
mysql.init_app(app)

from app import routes
