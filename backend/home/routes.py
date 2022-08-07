from flask import render_template
from backend.home import home
from backend.front_pack import front_pack


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
    return "to complete"
