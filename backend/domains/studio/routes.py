from backend.domains.studio import studio
from backend.front_pack import front_pack
from flask import render_template


@studio.route('/main')
def main():
    return render_template('domains/studio/main.html', front_pack=front_pack())


@studio.route('/pricing')
def pricing():
    return render_template('domains/studio/pricing.html')
