from flask import Blueprint

booking = Blueprint('booking', __name__, template_folder='templates', static_folder='static',
                    static_url_path='backend/static', url_prefix='/booking')

from backend.domains.booking import routes
