from sre_parse import _TemplateType
from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template("login.html", text="Testing", user="Kerim", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up')
def signup():
    return render_template("sign_up.html")