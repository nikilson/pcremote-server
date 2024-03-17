from flask import json
from flask import request
from app.oscontrols import bp
from utils.pc_controller import volume_up, volume_down

CONTENT_TYPE = {'ContentType': 'application/json'}

@bp.route('/volumeup/', methods=['GET'])
def volume_up_cnt():
    no_times = request.args.get("noTimes")
    try:
        no_times = int(no_times)
    except Exception as e:
        no_times = 1
    send_response = volume_up(no_times)
    return json.dumps({'success': True, 'message': send_response}), 200, CONTENT_TYPE


@bp.route('/volumedown/', methods=['GET'])
def volume_down_cnt():
    no_times = request.args.get("noTimes")
    try:
        no_times = int(no_times)
    except Exception as e:
        no_times = 1
    send_response = volume_down(no_times)
    return json.dumps({'success': True, 'message': send_response}), 200, CONTENT_TYPE
