# server/config.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData

# Create metadata for the database
metadata = MetaData()

# Create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Configure the database connection to the local file app.db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    
    # Configure flag to disable modification tracking and use less memory
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Create a Migrate object to manage schema modifications
    migrate = Migrate(app, db)
    
    # Initialize the Flask application to use the database
    db.init_app(app)
    
    return app

