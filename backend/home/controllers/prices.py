from sqlalchemy import desc, asc
from backend.app import db
from backend.models.models_prices import Prices, prices_schema, price_schema


class PricesControllers:
    @staticmethod
    def get_all_prices():
        return prices_schema.dump(Prices.query.order_by(asc(Prices.time_added)).all())

    @staticmethod
    def get_prices(limit=4):
        return prices_schema.dump(Prices.query.order_by(asc(Prices.time_added)).limit(limit))

    @staticmethod
    def get_price(name):
        return price_schema.jsonify(Prices.query.filter_by(name=name).first())

    def add_price(self, name, title, price, description, content, subscribe, discount, discount_code, discount_amount,
                  solo_price, beats_discount, beats_discount_code, beats_discount_amount):
        new_price = self.get_price(name)
        if new_price:
            return False
        new_price = Prices(
            name=name,
            title=title,
            price=price,
            description=description,
            content=content,
            subscribe=subscribe,
            discount=discount,
            discount_code=discount_code,
            discount_amount=discount_amount,
            solo_price=solo_price,
            beats_discount=beats_discount,
            beats_discount_code=beats_discount_code,
            beats_discount_amount=beats_discount_amount
        )
        db.session.add(new_price)
        db.session.commit()
        return True

    def modify_price(self, name, new_name, title, price, description, content, subscribe, discount, discount_code,
                     discount_amount, solo_price, beats_discount, beats_discount_code, beats_discount_amount):
        current_price = self.get_price(name)
        if current_price:
            current_price.name = new_name
            current_price.title = title
            current_price.price = price
            current_price.description = description
            current_price.content = content,
            current_price.subscribe = subscribe,
            current_price.discount = discount,
            current_price.discount_code = discount_code,
            current_price.discount_amount = discount_amount,
            current_price.solo_price = solo_price,
            current_price.beats_discount = beats_discount,
            current_price.beats_discount_code = beats_discount_code,
            current_price.beats_discount_amount = beats_discount_amount
            db.session.add(current_price)
            db.session.commit()
            return True
        return False

    def delete_service(self, name):
        price = self.get_price(name)
        if price:
            db.session.delete(price)
            db.session.commit()
            return True
        return False
