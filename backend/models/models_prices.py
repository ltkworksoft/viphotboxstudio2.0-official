from sqlalchemy import Column, String, Integer, DateTime, Boolean
from backend.app import db, marsh
from datetime import datetime as dt


class Prices(db.Model):
    __tablename__ = 'prices'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    title = Column(String)
    price = Column(Integer)
    description = Column(String)
    content = Column(String)
    subscribe = Column(Boolean, default=False)
    discount = Column(Boolean, default=False)
    discount_code = Column(String)
    discount_amount = Column(String)
    solo_price = Column(Boolean, default=False)
    beats_discount = Column(Boolean, default=False)
    beats_discount_code = Column(String)
    beats_discount_amount = Column(String)
    time_added = Column(DateTime, default=dt.now())

    def __init__(self, **kwargs):
        super(Prices, self).__init__(**kwargs)


class PricesSchema(marsh.Schema):
    class Meta:
        fields = ('name', 'title', 'price', 'description', 'content', 'subscribe', 'discount', 'discount_code',
                  'discount_amount', 'solo_price', 'beats_discount', 'beats_discount_code', 'beats_discount_amount')


price_schema = PricesSchema()
prices_schema = PricesSchema(many=True)
