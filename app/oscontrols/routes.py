from flask import json
from flask import request
from app.oscontrols import bp
from utils.pc_controller import volume_up


@bp.route('/volumeup/', methods=['GET'])
def volume_up_cnt():
    no_times = request.args.get("noTimes")
    try:
        no_times = int(no_times)
    except Exception as e:
        no_times = 1
    send_response = volume_up(no_times)
    return json.dumps({'success': True, 'message': send_response}), 200, {'ContentType': 'application/json'}


