from flask import Flask
from app.routes.main_routes import main_routes
from app.routes.users_routes import users_routes


def create_app():
    app = Flask(__name__)
    
    print("Registering users_routes...")


    app.register_blueprint(main_routes)
    app.register_blueprint(users_routes)
    
    return app
