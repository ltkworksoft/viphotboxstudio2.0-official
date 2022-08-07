from backend.domains.booking import booking
from flask import render_template


@booking.route('/main')
def main():
    return render_template('domains/booking/main.html', title="Réservation")
