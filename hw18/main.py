from view import app1
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Development")
    app1.register_blueprint(app1)