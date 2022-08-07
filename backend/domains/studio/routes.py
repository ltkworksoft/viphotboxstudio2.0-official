from backend.domains.studio import studio
from flask import render_template


@studio.route('/main')
def main():
    return render_template('domains/studio/main.html')


@studio.route('/pricing')
def pricing():
    return render_template('domains/studio/pricing.html')
