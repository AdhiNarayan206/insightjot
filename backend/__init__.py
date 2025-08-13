from flask import Flask
from flask_cors import CORS
from backend import pages
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    CORS(app)
    app.register_blueprint(pages.bp)
    return app