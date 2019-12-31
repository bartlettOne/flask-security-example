from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail

db = SQLAlchemy()
security = Security()
mail = Mail()

# Create app
def create_app():
    myapp = Flask(__name__)
    myapp.config['DEBUG'] = True
    myapp.config['SECRET_KEY'] = 'super-secret'
    myapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    # As of Flask-SQLAlchemy 2.4.0 it is easy to pass in options directly to the
    # underlying engine. This option makes sure that DB connections from the
    # pool are still valid. Important for entire application since
    # many DBaaS options automatically close idle connections.
    myapp.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
    }
    myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    myapp.config['SECURITY_PASSWORD_SALT'] = 'onetwothreefourfive'

    myapp.config['SECURITY_REGISTERABLE'] = True
    myapp.config['SECURITY_CONFIRMABLE'] = False
    myapp.config['SECURITY_RECOVERABLE'] = True
    myapp.config['SECURITY_TRACKABLE'] = True
    myapp.config['SECURITY_CHANGEABLE'] = True

    myapp.config['MAIL_SERVER']='localhost'
    myapp.config['MAIL_PORT']=8025

    db.init_app(myapp)
    mail.init_app(myapp)

    from app.models import User, Role
    from app.forms import ExtendedRegisterForm
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(myapp, user_datastore,
         register_form=ExtendedRegisterForm)

    from app.main import bp as main_bp
    myapp.register_blueprint(main_bp)


    # debug only for testing.
    app_context = myapp.app_context()
    app_context.push()
    db.create_all()
    user_datastore.create_user(email='test@me.com', password='password')
    db.session.commit()

    return myapp