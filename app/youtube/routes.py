from flask import json
from app.youtube import bp
from utils.whatkit import play_on_yt


@bp.route('/<string:search_key>/', methods=['GET'])
def play_on_yts(search_key=None):
    play_on_yt(search_key)
    if not search_key or len(search_key) <= 0:
        return json.dumps(
            {'success': False, 'errorMessage': 'Please provide valid search key: None Type not expected'}), 400, {
            'ContentType': 'application/json'}
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
