from flask import Blueprint

vids = Blueprint('vids', __name__, template_folder='templates', static_folder='static',
                 static_url_path='backend/static', url_prefix='/vids')
