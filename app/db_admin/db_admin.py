from app import db
from app import db_admin
from app.models import User, Role
from flask_admin.contrib.sqla import ModelView


db_admin.add_view(ModelView(Role, db.session))
db_admin.add_view(ModelView(User, db.session))
