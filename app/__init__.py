from flask import Flask

from config import Config
from app.main import bp as main_bp
from app.auth import bp as posts_bp
from app.youtube import bp as youtube_bp
from app.oscontrols import bp as os_controls_bp
from app.directorycontrol import bp as directory_bp
from utils.datamanager import get_value
from utils.directory_controller import cd_home_location


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initiate home location
    cd_home_location(get_value("HOME_LOCATION"))

    # Initialize Flask extensions here

    # Register blueprints here

    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp, url_prefix='/login/')
    app.register_blueprint(youtube_bp, url_prefix='/yt/')
    app.register_blueprint(os_controls_bp, url_prefix='/oscontrol/')
    app.register_blueprint(directory_bp, url_prefix='/dir/')


    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app