from sqlalchemy import desc, asc
from backend.app import db
from backend.models.models_basics import Partners, partner_schema, \
    partners_schema


class PartnersControllers:
    @staticmethod
    def get_all_partners():
        return partners_schema.dump(Partners.query.order_by(desc(Partners.id)).all())

    @staticmethod
    def get_partners(limit):
        return partners_schema.dump(Partners.query.order_by(asc(Partners.time_added)).limit(limit))

    @staticmethod
    def get_partner(name):
        return partner_schema.jsonify(Partners.query.filter_by(name=name).first())

    def add_service(self, name, img_path, img_alt, website):
        partner = self.get_partner(name)
        if partner:
            return False
        new_partner = Partners(
            name=name,
            img_path=img_path,
            img_alt=img_alt,
            website=website
        )
        db.session.add(new_partner)
        db.session.commit()
        return True

    def modify_partner(self, name, new_name, img_path, img_alt, website):
        partner = self.get_partner(name)
        if partner:
            partner.name = new_name
            partner.img_path = img_path
            partner.img_alt = img_alt
            partner.website = website
            db.session.add(partner)
            db.session.commit()
            return True
        return False

    def delete_partner(self, name):
        partner = self.get_partner(name)
        if partner:
            db.session.delete(partner)
            db.session.commit()
            return True
        return False
