from flask import Flask
from config import Config

from app.extensions import db, bcrypt, jwt

from app.auth.routes import auth_bp
from app.expenses.routes import expense_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(expense_bp)

    with app.app_context():
        db.create_all()

    return app