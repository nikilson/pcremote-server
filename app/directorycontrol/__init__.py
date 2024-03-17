from flask import Blueprint


bp = Blueprint('dir', __name__)
from app.directorycontrol import routes