from flask import Blueprint


bp = Blueprint('oscontrols', __name__)
from app.oscontrols import routes