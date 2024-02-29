import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = "Secret_Clave"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/prueba'
    SQLALCHEMY_TRACK_MODIFICATIONS = False