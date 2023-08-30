from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import requests
import os
import json

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
    discovery_url = os.environ['DISCOVERY_URL']
    service_name = os.environ['SERVICE_NAME']
    service_url = os.environ['SERVICE_URL']
    port = os.environ['PORT']

    connected_discover = False
    while not connected_discover:
        print("Registering cart service to discover")
        register_discover = requests.post(discovery_url, data={'service_name': service_name, 'service_port': port,
                                                               'service_url': service_url})
        print("register discover", register_discover.content)
        if json.loads(register_discover.content).get('success'):
            connected_discover = True

    migrate = Migrate(app, db, render_as_batch=True)
    return app