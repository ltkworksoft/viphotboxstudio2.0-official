from sqlalchemy import Column, String, Integer, Boolean, DateTime
from backend.app import db, marsh
from datetime import datetime as dt


class Offers(db.Model):
    __tablename__ = 'offers'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    title = Column(String)
    description = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    bg_color = Column(String)
    free = Column(Boolean, default=False)
    percentage = Column(Integer)
    time_added = Column(DateTime, default=dt.now())

    def __init__(self, **kwargs):
        super(Offers, self).__init__(**kwargs)


class OffersSchema(marsh.Schema):
    class Meta:
        fields = ('name', 'title', 'description', 'start_date', 'end_date', 'bg_color', 'free', 'percentage')


offer_schema = OffersSchema()
offers_schema = OffersSchema(many=True)
