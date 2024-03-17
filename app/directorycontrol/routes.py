from flask import json
from flask import request
from app.directorycontrol import bp
from utils.directory_controller import get_current_directory, list_working_directory
from os import path
from utils.datamanager import put_value

CONTENT_TYPE = {'ContentType': 'application/json'}


@bp.route('/pwd/', methods=['GET'])
def print_working_directory_cont():
    try:
        pwd = get_current_directory()
        return json.dumps({'success': True, 'pwd': pwd}), 200, CONTENT_TYPE
    except Exception as e:
        return json.dumps({'success': False, 'error': e}), 400, CONTENT_TYPE


@bp.route('/sethome/', methods=['POST'])
def set_home_directory_cont():
    directory = request.args.get("directory")
    if directory and path.isdir(directory):
        put_value("HOME_LOCATION", directory)
        response = f"The default directory {directory} has been set successfully!!!"
        return json.dumps({'success': True, 'message': response}), 200, CONTENT_TYPE
    return json.dumps({'success': False, 'error': "Please check the directory!"}), 400, CONTENT_TYPE


@bp.route('/ls/', methods=['GET'])
def list_working_directory_cont():
    try:
        pwd = get_current_directory()
        list_dir = list_working_directory(pwd)
        return json.dumps({'success': True, 'list': list_dir}), 200, CONTENT_TYPE
    except Exception as e:
        return json.dumps({'success': False, 'error': e}), 400, CONTENT_TYPE
