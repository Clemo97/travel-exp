from ensurepip import bootstrap
from flask import Flask



from config import config_options
 


# Initializing Flask Extensions






# bootstrap = Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # Initializing flask extensions
    # bootstrap.init_app(app)
     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from post import post as post_blueprint
    app.register_blueprint(post_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)


    # from .weathers import weather as weather_blueprint
    # app.register_blueprint(weather_blueprint)

    



    return app