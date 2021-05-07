import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                              '7b0342f12ee64296aaaa9738c72ca2c4'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://user:password@localhost:5432/department_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
