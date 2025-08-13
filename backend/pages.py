from flask import Blueprint
bp=Blueprint('pages',__name__)

@bp.route('/')
def home():
    return "Welcome to the Home Page"


@bp.route('/login')
def login():
    return "Welcome to the Login Page"