from flask import Blueprint


bp = Blueprint('youtube', __name__)
from app.youtube import routes