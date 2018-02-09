class Config:
    '''General Configuration'''
    pass


class ProdConfig(Config):
    '''Production configuration child class'''
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
 'development': DevConfig,
 'production': ProdConfig
}
