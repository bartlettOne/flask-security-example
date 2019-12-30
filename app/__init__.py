from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

db = SQLAlchemy()
security = Security()

# Create app
def create_app():
    myapp = Flask(__name__)
    myapp.config['DEBUG'] = True
    myapp.config['SECRET_KEY'] = 'super-secret'
    myapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    myapp.config['SECURITY_PASSWORD_SALT'] = 'onetwothreefourfive'

    db.init_app(myapp)

    from app.models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(myapp, user_datastore)

    from app.main import bp as main_bp
    myapp.register_blueprint(main_bp)


    # debug only for testing.
    app_context = myapp.app_context()
    app_context.push()
    db.create_all()
    user_datastore.create_user(email='matt@nobien.net', password='password')
    db.session.commit()

    return myapp