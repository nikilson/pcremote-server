from app import create_app
from config import Config
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    app = create_app(config_class=Config)
    host_ip = os.getenv("HOST_IP_ADDRESS") or 'localhost'
    app.run(debug=True, host=host_ip)