from nis import cat
from sre_parse import _TemplateType
from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    #data will be printed as a immutable dicted object in the terminal
    return render_template("login.html", text="Testing", user="Kerim", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #check if valid
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('first name must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('passwords do not match', category='error')
        elif len(password1) <7:
            flash('password must be greater than 6 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            #add user to database
            db.session.add(new_user)
            db,session.comit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
#flash messages do not currently display 

    return render_template("sign_up.html")

