from flask import Blueprint

studio = Blueprint('studio', __name__, template_folder='templates', static_folder='static',
                   static_url_path='backend/static', url_prefix='/studio')

from backend.domains.studio import routes
