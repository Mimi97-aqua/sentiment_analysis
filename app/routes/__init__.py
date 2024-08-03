from flask import Flask
from .sentiment_routes import sentiment_routes


def create_app():
    app = Flask(__name__)

    app.register_blueprint(sentiment_routes, url_prefix='/api')

    return app
