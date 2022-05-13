from sre_parse import _TemplateType
from flask import Blueprint, render_template, request

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
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) <7:
            pass
        else:
            #add user to database
            pass


    return render_template("sign_up.html")

