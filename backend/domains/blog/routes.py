from backend.domains.blog import blog
from flask import render_template


@blog.route('/main')
def main():
    return render_template('domains/blog/main.html', title="Blog")
