from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
DB_NAME = "expensesDB.CS.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "ahsdfhsdf ahdsfdsh"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)


    app.config['DEBUG'] = True
    app.config['TESTING'] = False
    app.config['MAIL_SERVER'] = "localhost"
    app.config['MAIL_PORT'] = 25
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEBUG'] = True
    app.config['MAIL_USERNAME'] = '"owusu_ys@soshgic.edu.gh"'
    app.config['MAIL_PASSWORD'] = 'allrosegold'
    app.config['MAIL_DEFAULT_SENDER'] = "owusu_ys@soshgic.edu.gh"
    app.config['MAIL_MAX_EMAILS'] = None
    #app.config['MAIL_SUPPRESS_SEND'] = False
    app.config['MAIL_ASCII ATTACHMENTS'] = False

    mail = Mail(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
 
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")