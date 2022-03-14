from flask import Flask

def create_app():
    app = Flash(__name__)
    app.config['SECRETE_KEY'] = "This is the key"

    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app
