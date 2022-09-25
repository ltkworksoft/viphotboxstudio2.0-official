from flask import render_template
from backend.home import home
from backend.front_pack import front_pack
from backend.home.controllers.messages import MessagesControllers
from backend.home.forms import SendMessageForm


@home.route('/')
@home.route('/home')
@home.route('/index')
def index():
    return render_template('home/index.html', title="Accueil", front_pack=front_pack())


@home.route('/about')
def about():
    return render_template('home/about.html', title="À propos", front_pack=front_pack())


@home.route('/contacts')
def contacts():
    return render_template('home/contacts.html', title="Contacts", front_pack=front_pack())


@home.route('/send_message')
def send_message():
    return render_template('home/send_message.html', title="Envoyer un message", front_pack=front_pack())


@home.route('/send_message', methods=["POST"])
def send_message_post():
    form = SendMessageForm()
    name = form.name.data
    email = form.email.data
    category = form.category.data
    message = form.message.data
    return MessagesControllers.send_message(name, email, category, message)

@home.route('/gal')
def gal():
    return render_template('components/gallery.html', front_pack=front_pack())