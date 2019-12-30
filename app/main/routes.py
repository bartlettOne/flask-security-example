from app import db
from flask_security import login_required
from app.main import bp
from flask import render_template

# Views
@bp.route('/')
@login_required
def home():
    return render_template('index.html')
