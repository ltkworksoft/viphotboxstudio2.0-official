from flask import Blueprint, redirect, url_for
from backend.app import login_manager

user = Blueprint('user', __name__, template_folder='templates', static_folder='static',
                 static_url_path='backend/static', url_prefix='/user')

login_manager.session_protection = 'strong'
login_manager.login_message = 'Veuillez vous connecter avant d\'accéder au contenu de cette page.'
login_manager.login_message_category = 'info'
login_manager.login_view = 'user.login'
login_manager.refresh_view = 'user.re_login'
login_manager.needs_refresh_message = "Session timeout, please re-login"
login_manager.needs_refresh_message_category = "info"


# login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def user_loader(public_id):
    return 'User.query.get(public_id)'


@login_manager.needs_refresh_handler
def refresh():
    return redirect(url_for('user.re_login'))
