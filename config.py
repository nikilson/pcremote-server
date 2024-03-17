import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not os.path.exists(os.path.join(basedir, 'data')):
        os.makedirs(os.path.join(basedir, 'data'))
    SHELVE_URI = os.path.join(basedir, 'data', 'app')
