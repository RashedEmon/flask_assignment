#Standard library imports.
from logging import root
from multiprocessing import current_process
import os
import secrets
#Related third party imports.
from flask import Flask,current_app, redirect,url_for
from flask_login import current_user
#Local application specific imports.
from flask_root.auth import bp,error_handler_404, login_manager
from flask_root.post import post_bp
from flask_root.dashboard import dashboardbp

#This is the entry point of the application.
def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,template_folder='templates')

    
    secret_key = secrets.token_urlsafe(16)
    if os.getenv('SECRET_KEY') == None:
        os.environ['SECRET_KEY'] = secret_key

    app.config.from_mapping(
        {
            'SECRET_KEY': os.getenv('SECRET_KEY')
        }
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def home():
        return redirect(url_for('/login.login'))

    #register blueprints with app instance
    app.register_blueprint(bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(dashboardbp)

    #register error handling with app instance
    app.register_error_handler(404,error_handler_404)

    #register login manager with app instance
    login_manager.init_app(app)
    return app
