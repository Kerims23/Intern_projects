from nis import cat
from sre_parse import _TemplateType
from unicodedata import category
from flask import Blueprint, render_template, request, flash

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
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #check if valid
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('first name must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('passwords do not match', category='error')
        elif len(password1) <7:
            flash('password must be greater than 6 characters', category='error')
        else:
            #add user to database
            flash('Account created!', category='success')


    return render_template("sign_up.html")

