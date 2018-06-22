import os
basedir = os.path.abspath(os.path.dirname(__file__))
"""Development Environment"""
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG= True


class DevelopmentConfig(Config):
    DEBUG= True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False


config = {
    'development':DevelopmentConfig,
    'testinng':TestingConfig,
    'production':ProductionConfig,
    'default': DevelopmentConfig
     }

