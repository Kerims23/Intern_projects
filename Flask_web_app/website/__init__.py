from flask import Flask

def create_app():
    app = Flash(__name__)
    app.config['SECRETE_KEY'] = "This is the key"

    return app
    