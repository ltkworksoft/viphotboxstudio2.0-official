from flask import Blueprint

api = Blueprint('api', __name__, template_folder='templates', static_folder='static', static_url_path='backend/static',
                url_prefix='/api')

from backend.api import errors
