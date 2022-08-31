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


@home.route('/send_message', methods=["POST"])
def send_message():
    form = SendMessageForm()
    name = form.name.data
    email = form.email.data
    category = form.category.data
    message = form.message.data
    return MessagesControllers.send_message(name, email, category, message)


@home.route('/doc')
def doc():
    return render_template('doc.html', front_pack=front_pack())
