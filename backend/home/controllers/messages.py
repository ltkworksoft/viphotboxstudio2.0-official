from flask import url_for, request
from sqlalchemy import desc, asc
from werkzeug.utils import redirect
from backend.email import send_mail
from backend.app import db
from backend.models.models_basics import Messages, message_schema, messages_schema


class MessagesControllers:
    @staticmethod
    def send_message(name, email, category, message):
        new_message = Messages(
            name=name,
            email=email,
            category=category,
            message=message
        )
        db.session.add(new_message)
        db.session.commit()
        send_mail(email, "Ne pas répondre", "email/email_message", message=new_message)
        return redirect(request.referrer)
