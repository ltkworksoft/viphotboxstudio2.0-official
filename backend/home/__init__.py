from flask import Blueprint

home = Blueprint('home', __name__, template_folder='templates', static_folder='static',
                 static_url_path='backend/static', url_prefix='/')

from backend.home import routes, forms
from backend.home.controllers import services, partners, messages

