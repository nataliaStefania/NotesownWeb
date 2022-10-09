from decouple import config
'''from matplotlib.offsetbox import DEBUG'''

class Config:
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True
config = {
    'development': DevelopmentConfig
}