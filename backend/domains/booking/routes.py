from backend.domains.booking import booking
from flask import render_template

from backend.front_pack import front_pack


@booking.route('/main')
def main():
    return render_template('domains/booking/main.html', title="Réservation", front_pack=front_pack())


@booking.route('/confirmation')
def confirmation():
    return render_template('domains/booking/confirmation.html', title="Confirmation de réservation", front_pack=front_pack())
