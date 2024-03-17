from app import create_app
from config import Config

if __name__ == '__main__':
    app = create_app(config_class=Config)
    app.run(debug=True)