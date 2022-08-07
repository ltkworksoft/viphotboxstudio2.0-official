from flask import Blueprint

offers = Blueprint('offers', __name__, template_folder='templates', static_folder='static',
                   static_url_path='backend/static', url_prefix='/offers')


from backend.domains.offers import routes
