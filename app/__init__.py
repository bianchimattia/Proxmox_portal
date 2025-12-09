import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.py')
    app.config.from_pyfile(config_path)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Blueprint
    from .routes.main import main_bp
    from .routes.auth import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Import User per il login
    from .models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
