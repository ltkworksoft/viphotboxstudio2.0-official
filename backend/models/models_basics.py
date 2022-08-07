from sqlalchemy import Column, String, Integer, DateTime, Boolean
from backend.app import db, marsh
from datetime import datetime as dt


class Messages(db.Model):
    __tablename__ = 'messages'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    email = Column(String(100))
    category = Column(String(100))
    message = Column(String(500))
    time_sent = Column(DateTime, default=dt.now())
    responded = Column(Boolean, default=False)
    time_responded = Column(DateTime)
    responder_id = Column(String(32))
    archived = Column(Boolean, default=False)

    def __init__(self, **kwargs):
        super(Messages, self).__init__(**kwargs)


class MessagesSchema(marsh.Schema):
    class Meta:
        fields = ('name', 'email', 'category', 'message', 'time_sent', 'responded', 'time_responded', 'responder_id',
                  'archived')


message_schema = MessagesSchema()
messages_schema = MessagesSchema(many=True)


class Services(db.Model):
    __tablename__ = 'services'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100))
    title = Column(String(200))
    description = Column(String(500))
    icon = Column(String(100))
    time_added = Column(DateTime, default=dt.now())

    def __init__(self, **kwargs):
        super(Services, self).__init__(**kwargs)


class ServicesSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name', 'title', 'description', 'icon')


service_schema = ServicesSchema()
services_schema = ServicesSchema(many=True)


class Partners(db.Model):
    __tablename__ = 'partners'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100))
    img_path = Column(String)
    img_alt = Column(String)
    website = Column(String)
    time_added = Column(DateTime, default=dt.now())

    def __init__(self, **kwargs):
        super(Partners, self).__init__(**kwargs)


class PartnersSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name', 'img_path', 'img_alt', 'website')


partner_schema = PartnersSchema()
partners_schema = PartnersSchema(many=True)
