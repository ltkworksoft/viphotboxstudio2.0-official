from sqlalchemy import Column, String, Integer, Boolean, DateTime
from backend.app import db, marsh
from datetime import datetime as dt


class Booking(db.Model):
    __tablename__ = 'booking'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String)
    start_hour = Column(String)
    end_hour = Column(String)
    session_type = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    artist_name = Column(String)
    phone = Column(String)
    instagram = Column(String)
    time_added = Column(DateTime, default=dt.now())

    def __init__(self, **kwargs):
        super(Booking, self).__init__(**kwargs)
