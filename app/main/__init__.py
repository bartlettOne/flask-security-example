from flask import Blueprint

bp = Blueprint('main', __name__)

# import the routes.py module, so that the main routes
# in it are registered with the blueprint. This import is at 
# the bottom to avoid circular dependencies.
from app.main import routes