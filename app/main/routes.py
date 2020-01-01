from app import db#, user_datastore
from flask_security import login_required
from app.main import bp
from flask import render_template
#from flask_security.signals import user_registered

# Views
@bp.route('/')
@login_required
def home():
    return render_template('index.html')

# # @user_registered.connect_via(current_app)
# def user_registered_sighandler(app_sender, user, confirm_token):
#     default_role = user_datastore.find_role("user")
#     user_datastore.add_role_to_user(user, default_role)
#     db.session.commit()

