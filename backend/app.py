from flask import Flask, session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from backend.settings import settings

login_manager = LoginManager()
mail = Mail()
db = SQLAlchemy()
marsh = Marshmallow()
mig = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    settings.select_environment_config(app, app.config['ENV'])
    print(f"ENV is set to {app.config['ENV']}")

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        SSLify(app)

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    marsh.init_app(app)
    mig.init_app(app, db)

    from backend.home import home
    from backend.api import api
    from backend.api.errors import page_not_found, forbidden, internal_server_error
    from backend.domains import domains
    from backend.vip import vip
    from backend.user import user
    # from backend.models.user import User, AnonymousUser

    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = app.config['PERMANENT_SESSION_LIFETIME']

    app.register_blueprint(home)
    app.register_blueprint(api)
    app.register_blueprint(domains)
    app.register_blueprint(vip)
    app.register_blueprint(user)

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, forbidden)
    app.register_error_handler(500, internal_server_error)

    with app.app_context():
        if app.config['ENV'] == 'development':
            db.create_all()
            return app
        return app

