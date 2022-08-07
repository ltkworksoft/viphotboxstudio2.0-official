from flask import Blueprint

medias = Blueprint('medias', __name__, template_folder='templates', static_folder='static',
                   static_url_path='backend/static', url_prefix='/medias')

from backend.domains.medias.photos import photos
from backend.domains.medias.vids import vids
from backend.domains.medias.audio import audio

medias.register_blueprint(photos)
medias.register_blueprint(vids)
medias.register_blueprint(audio)
