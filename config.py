import os


class Config:
    '''General Configuration'''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://TevinMilla:1234#@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    '''Production configuration child class'''
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
 'development': DevConfig,
 'production': ProdConfig
}
