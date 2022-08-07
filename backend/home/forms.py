from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class SendMessageForm(FlaskForm):
    name = StringField("Nom Complet", validators=[DataRequired(), Length(1, 64)])
    email = StringField("Adresse Courriel", validators=[DataRequired(),
                                                        Email(message="Veuillez entrer une adresse courriel valide!"),
                                                        Length(1, 100)])
    category = SelectField("Catégorie", validators=[DataRequired()],
                           choices=[
                               "Informations",
                               "Informations sur le prix",
                               "Problème durant la réservation",
                               "Un projet",
                               "Autre"
                           ])
    message = TextAreaField("Message", validators=[DataRequired(), Length(1, 500)])
    submit = SubmitField("Envoyer")
