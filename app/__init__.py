# from flask import Flask
# from flask_bootstrap import Bootstrap
# from config import config_options

# bootstrap = Bootstrap()

# def create_app(config_name):

#     # Initialising application
#     app = Flask(__name__)

#     # Creating the app configurations
#     app.config.from_object(config_options[config_name])

#     # Initialising flask extensions
#     bootstrap.init_app(app)

#     # Reqistering the blueprint
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     # Setting config
#     from .request import configure_request
#     configure_request(app)

#     return app
