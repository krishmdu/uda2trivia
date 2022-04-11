import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/fyyur2'
SQLALCHEMY_TRACK_MODIFICATIONS = False 

# APP_ENABLE_SECURE_HEADERS = False
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = True