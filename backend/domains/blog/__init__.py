from flask import Blueprint

blog = Blueprint('blog', __name__, template_folder='templates', static_folder='static',
                 static_url_path='backend/static', url_prefix='/blog')

from backend.domains.blog import routes
