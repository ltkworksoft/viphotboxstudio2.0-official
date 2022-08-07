from sqlalchemy import desc, asc
from backend.app import db
from backend.models.models_offers import Offers, offer_schema, offers_schema


class OffersControllers:
    @staticmethod
    def get_all_offers():
        return offers_schema.dump(Offers.query.order_by(desc(Offers.id)).all())

    @staticmethod
    def get_offers(limit):
        return offers_schema.dump(Offers.query.order_by(asc(Offers.time_added)).limit(limit))

    @staticmethod
    def get_offer(name):
        return offer_schema.jsonify(Offers.query.filter_by(name=name).first())

    def add_offer(self, name, title, description, start_date, end_date, bg_color, free, percentage):
        offer = self.get_offer(name)
        if offer:
            return False
        new_offer = Offers(
            name=name,
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            bg_color=bg_color,
            free=free,
            percentage=percentage
        )
        db.session.add(new_offer)
        db.session.commit()
        return True

    def modify_offer(self, name, new_name, title, description, start_date, end_date, bg_color, free, percentage):
        offer = self.get_offer(name)
        if offer:
            offer.name = new_name
            offer.title = title
            offer.description = description
            offer.start_date = start_date
            offer.end_date = end_date
            offer.bg_color = bg_color
            offer.free = free
            offer.percentage = percentage
            db.session.add(offer)
            db.session.commit()
            return True
        return False

    def delete_offer(self, name):
        offer = self.get_offer(name)
        if offer:
            db.session.delete(offer)
            db.session.commit()
            return True
        return False
