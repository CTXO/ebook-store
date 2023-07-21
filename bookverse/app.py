from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def create_app():
    from .user.models import User
    from .ebook.models import Ebook
    from .cart.models import Cart

    from .gui.controllers_frontend import controller
    app = Flask(__name__, template_folder='./gui/templates', static_folder='./gui/static')
    app.secret_key = b'dfoahioadsl2342/*//34382ldslkj#$%$#$%$#%$#%490'

    app.register_blueprint(controller)


    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookverse.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
    return app
