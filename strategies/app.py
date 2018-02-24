from flask import Flask
from strategies.blueprints.two_assets_MA import two_assets_MA

def create_app():
    """
    Crea una aplicacion de flask usando patron de fábrica.

    :return: Flask app
    """

    # configuracion de la aplicacion
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    # blueprints
    app.register_blueprint(two_assets_MA)

    return app
