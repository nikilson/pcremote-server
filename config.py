import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SHELVE_URI = os.environ.get('SHELVE_URI') or os.path.join(basedir, 'app')
