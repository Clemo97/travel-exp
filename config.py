import os

import app


class Config:
    """
    General parent configuration parent class
    """
    SECRET_KEY ='123456789'
    
    SQLALCHEMY_DATABASE_URI = ''
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
   
class ProdConfig(Config):
   
    
    DEBUG= True


class DevConfig(Config):
    
    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}