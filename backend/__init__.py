from flask import Flask
from flask_cors import CORS
from backend import pages
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(pages.bp)
    return app