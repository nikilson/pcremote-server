from flask import Flask

from config import Config
from app.main import bp as main_bp
from app.auth import bp as posts_bp
from app.youtube import bp as youtube_bp
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here

    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp, url_prefix='/login/')
    app.register_blueprint(youtube_bp, url_prefix='/yt/')


    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app