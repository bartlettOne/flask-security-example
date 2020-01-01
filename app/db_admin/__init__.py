
from flask import Blueprint

bp = Blueprint('db_admin', __name__)

# import the routes.py module, so that the admin routes
# in it are registered with the blueprint. This import is at 
# the bottom to avoid circular dependencies.
from app.db_admin import db_admin
