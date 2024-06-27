import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    FORECAST_ENDPOINT = os.environ.get('GET_FORECAST_URL') or \
        'http://127.0.0.1:5000/get_forecast'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    FORECAST_ENDPOINT = os.environ.get('GET_FORECAST_URL') or \
        'https://svs-data-analyzer-35d8f53ed4b0.herokuapp.com/get_forecast'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig

}
