from flask import Flask

# from flask_bootstrap import Bootstrap

from config import config_options
from flask_sqlalchemy import SQLAlchemy 


# Initializing Flask Extensions

db = SQLAlchemy




# bootstrap = Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # Initializing flask extensions
    # bootstrap.init_app(app)
    # Registering the blueprint
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from post import post as post_blueprint
    app.register_blueprint(post_blueprint)

    from .weathers import weather as weather_blueprint
    app.register_blueprint(weather_blueprint)

    



    return app