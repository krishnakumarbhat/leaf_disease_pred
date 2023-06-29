from flask import Flask

def create_app():
    # Create the Flask application
    app = Flask(__name__)

    # Register blueprints
    from .views import views
    app.register_blueprint(views)

    return app
