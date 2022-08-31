from datetime import datetime as dt
from backend.data import vip_address, vip_emails, vip_phones, social_medias, send_message_categories, open_hours, \
    production_team, liste, discount_amount, charge, invoice
from backend.home.controllers.services import ServicesControllers
from backend.home.controllers.partners import PartnersControllers
from backend.controllers.controllers import OffersControllers
from backend.home.controllers.prices import PricesControllers
from backend.controllers.controllers_videos import VideosControllers
from backend.home.forms import SendMessageForm
from backend.settings import settings


def front_pack():
    return {
        'settings': settings,
        'current_year': dt.now().year,
        'address': vip_address,
        'email': vip_emails,
        'phone': vip_phones,
        'social_medias': social_medias,
        'message_category': send_message_categories,
        'open_hours': open_hours,
        'services': ServicesControllers(),
        'partners': PartnersControllers(),
        'offers': OffersControllers(),
        'prices': PricesControllers(),
        'production_team': production_team,
        'videos': VideosControllers,
        'message_form': SendMessageForm(),
        'liste': liste,
        'discount_amount': discount_amount,
        'charge': charge,
        'invoice': invoice(liste, discount_amount, charge)
    }
