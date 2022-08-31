from backend.domains.booking import booking
from flask import render_template

from backend.front_pack import front_pack


@booking.route('/main')
def main():
    return render_template('domains/booking/main.html', title="Réservation", front_pack=front_pack())
