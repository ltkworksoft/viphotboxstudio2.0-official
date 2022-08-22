from sqlalchemy import Column, String, Integer, DateTime, Boolean
from backend.app import db, marsh
from datetime import datetime as dt


class Videos(db.Model):
    __tablename__ = 'videos'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String)
    displayed = Column(Boolean, default=True)
    display_on = Column(DateTime, default=dt.now())
    time_added = Column(DateTime, default=dt.now())

    def __init__(self, **kwargs):
        super(Videos, self).__init__(**kwargs)


class VideosSchema(marsh.Schema):
    class Meta:
        fields = ('link', 'displayed', 'displayed_on')


video_schema = VideosSchema()
videos_schema = VideosSchema(many=True)
