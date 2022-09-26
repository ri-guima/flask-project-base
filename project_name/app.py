from flask import Flask
from dynaconf import FlaskDynaconf


def create_app() -> Flask:
    app = Flask(__name__, static_folder='static', template_folder='templates')
    FlaskDynaconf(app, extensions_list='EXTENSIONS')
    return app
