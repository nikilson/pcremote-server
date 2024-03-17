import shelve
from config import Config


def put_value(key, value):
    with shelve.open(Config.SHELVE_URI) as db:
        db[key] = value


def get_value(key):
    with shelve.open(Config.SHELVE_URI) as db:
        value = db.get(key)
    return value
