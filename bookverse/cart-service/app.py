from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import configs
db = SQLAlchemy()

def create_app():
    from .models.models import Cart
    from .models.models import Ebook

    from .gui.controllers_frontend import controller
    app = Flask(__name__, template_folder='./gui/templates', static_folder='./gui/static')
    app.secret_key = b'dfoahioadsl2342/*//34382ldslkj#$%$#$%$#%$#%490'

    app.register_blueprint(controller)
    app.config.update(configs)

    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
    return app
