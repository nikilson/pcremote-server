from flask import json
from app.youtube import bp
from utils.whatkit import play_on_yt

@bp.route('/<string:search_key>/', methods=['GET'])
def play_on_yts(search_key=None):
    play_on_yt(search_key)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}