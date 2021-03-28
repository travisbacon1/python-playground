from flask import Flask

# Globally accessible libraries would go here
# i.e. MySQL - not required in this example


def create_app():
    """Initialise the core application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    # i.e. a MySQL database plugin

    with app.app_context():
        # Include our routes
        from .home.home import home
        from .about.about import about

        # Register Blueprints
        app.register_blueprint(home)
        app.register_blueprint(about)

        return app