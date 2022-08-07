from flask import Blueprint

domains = Blueprint('domains', __name__, template_folder='templates', static_folder='static',
                    static_url_path='source/static', url_prefix='/domains')

from backend.domains.booking import booking
from backend.domains.studio import studio
from backend.domains.blog import blog
from backend.domains.events import events
from backend.domains.medias import medias
from backend.domains.offers import offers

domains.register_blueprint(booking)
domains.register_blueprint(studio)
domains.register_blueprint(blog)
domains.register_blueprint(events)
domains.register_blueprint(medias)
domains.register_blueprint(offers)
