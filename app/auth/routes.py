from flask import render_template
from app.auth import bp

@bp.route('/')
def login():
    return render_template('login.html')